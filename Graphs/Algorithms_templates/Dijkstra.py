from queue import PriorityQueue

def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[s] = 0 # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    pq.put((d[s], s))

    # Main loop:
    while(not pq.empty()):
        prio, vertex = pq.get()
        if(vertex == end):
            return parent
        if(prio <= d[vertex]): # We check the vertex only if we haven't already found a better path
            visited[vertex] = True
            # Relaxation for the newly found vertex:
            for (v, length) in G[vertex]:
                if(d[v] > d[vertex] + length and visited[v] == False):
                    d[v] = d[vertex] + length
                    parent[v] = vertex
                    pq.put((d[v], v))
    return None

inf = float("inf")
G=[
    [(1, 2), (4, 2)],
    [(0, 2), (2, 3), (4, 1), (5, 8)],
    [(1, 3), (3, 1)],
    [(2, 1), (4, 5), (5, 1)],
    [(0, 2), (1, 1), (3, 5)],
    [(1, 8), (3, 1)]
]

start = 0
end = 5
path = dijkstra(G, start, end)

while(end != start):
    print(end, end=" <--- ")
    end = path[end]
print(end)