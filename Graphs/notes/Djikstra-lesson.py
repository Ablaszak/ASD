def dijktra(G, s):
    # Initialization:
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[s] = 0
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
            return True # Because there are no more vertexes to
        # Now we know that the vertex exists and we can visit it
        visited[vertex] = True

        # Relaxation for the just found vertex:
        for v in range(n):
            if(G[vertex][v] is not None):
                if(d[v] > d[vertex] + G[vertex][v]):
                    parent[v] = v
                    d[v] = d[vertex] + G[vertex][v]

G=[

]
