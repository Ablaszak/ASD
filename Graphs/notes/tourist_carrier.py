"""
We have a tourist carrier who wants to drive between vertexes A and B.

Every edge is a bus that can carry up to W people (where W = weight(edge))

The carrier wants to find such path, where he can transport the biggest
amount of people in one group
(Path with biggest smallest edge weight)


"""

from queue import PriorityQueue

def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    parent = [None for _ in range(n)]
    d = [0 for _ in range(n)] # min bus capacity (negative to get the biggest abs value)
    d[s] = -float("inf") # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    pq.put((d[s], s))

    # Main loop:
    while(not pq.empty()):
        prio, vertex = pq.get()
        if(vertex == end):
            return parent, abs(prio)
        if(abs(prio) <= abs(d[vertex])): # We check the vertex only if we haven't already found a better path
            visited[vertex] = True
            # Relaxation for the newly found vertex:
            for (v, length) in G[vertex]:
                length *= -1
                if(d[v] > max(d[vertex], length) and visited[v] == False):
                    d[v] = max(d[vertex], length)
                    parent[v] = vertex
                    pq.put((d[v], v))
    return None

inf = float("inf")
G=[
    [(1, 1), (3, 20)],
    [(0, 1), (2, 0)],
    [(1,0), 6,20],
    [(0,20), (4,20)],
    [(3, 20), (5,20)],
    [(4,20), (6,20)],
    [(5,20), (2,20)]
]

start = 0
end = 2
path, cap = dijkstra(G, start, end)
print(cap)
while(end != start):
    print(end, end=" <--- ")
    end = path[end]
print(end)