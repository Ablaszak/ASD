def dijkstra(G, s=0):
    # Initialization:
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[s] = 0 # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]

    # Main loop:
    while(True):
        vertex = -1
        nearest = float("inf")
        for i in range(n):
            # Looking for nearest to s, not yet visited vertex:
            if(d[i] < nearest and visited[i] == False):
                nearest = d[i]
                vertex = i
        if(vertex == -1):
            return parent # Because there are no more vertexes to
        # Now we know that the vertex exists and we can visit it
        visited[vertex] = True

        # Relaxation for the newly found vertex:
        for v in range(n):
            if(G[vertex][v] is not None and (vertex != v)):
                if(d[v] > d[vertex] + G[vertex][v]):
                    d[v] = d[vertex] + G[vertex][v]
                    parent[v] = vertex

inf = float("inf")
G=[
    [0, 2, None, None, 2, None],
    [2, 0, 3, None, 1, 8],
    [None, 3, 0, 1, None, None],
    [None, None, 1, 0, 5, 1],
    [2, 1, None, 5, 0, None],
    [None, 8, None, 1, None, 0]
]

start = 0
end = 5
path = dijkstra(G, start)
#print(path)
while(end != start):
    print(end, end=" <-- ")
    end = path[end]
print(start)
