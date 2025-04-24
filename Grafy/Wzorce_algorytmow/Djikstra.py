def relaxation(G, u, v):


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
            if(d[i] < j):
                d_nei = d[i]
                neighbour = i
        if(neighbour == -1):
            return parent[s]
        # Now we know that the vertex exists
        visited[neighbour] = True

        # Relaxation:
        for i in range(n):
            if(G[neighbour][i] is not None):
                if(d[i] > d[neighbour] + G[neighbour][i])
                    parent[i] = u
                    d[i] = d[neighbour] + G[neighbour][i]


