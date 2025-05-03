"""
Problem:
We have a map of a country in form of a graph, where vertexes are cities.
There are two drivers in a car, they change in every city on the way.
Find a path, where driver #0 drives for the shortest time (driver #1 can ride as lond as he wants)

Idea:
We can search for paths, but we have to count two things:
    1) sum length of even edges
    2) sum length of odd edges

    In the end we choose which length we prefer (shorter one)

Better:
Each city has two vertexes (doubles), one is for #0 entering city, second vertex is for #1"
"""

from queue import PriorityQueue

def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    parent = [[None, None] for _ in range(n)] # Index depends on who drove previous edge
    d = [[float("inf"), float("inf")] for _ in range(n)]
    d[s] = [0, 0]  # <--- Very important, without this the algorithm won't start
    # Note: now d[s] is not a total distance, but dstance driven by driver#1
    visited = [[False, False] for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, 0)) # last driver: #0 (so #1 will drive next edge)
    pq.put((0, s, 1)) # last driver: #1

    # Main loop:
    while (not pq.empty()):
        prio, vertex, driver = pq.get()
        if (vertex == end):
            return parent, driver # Last driver
        visited[vertex][driver] = True
        # Relaxation for the newly found vertex:
        for (v, length) in G[vertex]:
            if(driver == 1): # #1 came to vertex, #0 will drive now
                if(d[v][0] > d[vertex][1] + length):
                    d[v][0] = d[vertex][1] + length
                    parent[v][0] = vertex
                    pq.put((d[v][0], v, 0))
            else: # #0 came to vertex, #1 will drive now
                if(d[v][1] > d[vertex][0]):
                    d[v][1] = d[vertex][0] # We don't add enything, because #0 is not driving
                    parent[v][1] = vertex
                    pq.put((d[v][1], v, 1))
    return None


inf = float("inf")
G = [
    [(1,10), (3,1)],
    [(2,10)],
    [],
    [(4,10)],
    [(2,1)]
]

start = 0
end = 2
path, driver = dijkstra(G, start, end)

while(end != start):
    print(end, end=" <--- ")
    end = path[end][driver]
    driver = (driver+1)%2

print(start)