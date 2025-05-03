def djiktra(G, s):
    # Initialization:
    n = len(G)
    parent = [ None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[s] = 0
    visited = [False for _ in range(n)]

    # Main loop:
    while(True):
        # Looking for smallest d value
        neighbour = -1
        d_nei = float("inf")
        for i in range(n):
            # Looking for least remote, not visited vertex:
            if(d[i] < d_nei and visited[i] == False):
                d_nei = d[i]
                neighbour = i
        if(neighbour == -1):
            return True
        # Now we know that the vertex exists
        visited[neighbour] = True

        # Relaxation for neighbour:
        for v in range(n):
            if(G[neighbour][v] is not None):
                if(d[v] > d[neighbour] + G[neighbour][v]):
                    parent[v] = v
                    d[v] = d[neighbour] + G[neighbour][v]


