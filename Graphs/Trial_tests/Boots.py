from queue import PriorityQueue

def rewrite(M):
    N = False # Normal
    J = True  # Jump
    n = len(M)
    adj = [[] for _ in range(n)]
    for u in range(n):
        for v in range(u): # since we know the graph is undirected
            if(M[u][v] != 0):
                adj[u].append( [v, M[u][v], N] )
                adj[v].append( [u, M[u][v], N] )

    # Now we add jumping edges:
    for u in range(n):
        for v1, w1, way1 in adj[u]:
            for v2, w2, way2 in adj[v1]:
                if(v2 != u and way1==way2==N):
                    adj[u].append( [v2, max(w1, w2), J] )
    return adj, n

def jumper(G, s, end):
    # Initialization:
    N = False # Normal
    J = True  # Jump

    G, n = rewrite(G)

    parent = [None for _ in range(n)]
    dN = [float("inf") for _ in range(n)]
    dJ = [float("inf") for _ in range(n)]
    dN[s] = dJ[s] = 0 # <--- Very important, without this the algorithm won't start
    visited = [[False, False] for _ in range(n)]
    pq = PriorityQueue()
    pq.put([dN[s], s, N]) # Last var tells how we got here

    # Main loop:
    while(not pq.empty()):
        prio, vertex, how = pq.get()

        if(vertex == end):
            return prio

        if((how == N and prio <= dN[vertex]) or (how == J and prio <= dJ[vertex])): # We check the vertex only if we haven't already found a better path
            visited[vertex][how] = True
            # Relaxation for the newly found vertex:
            for (v, length, NJ) in G[vertex]:
                # we can always walk:
                if(NJ == N and dN[v] > prio + length and visited[v][NJ] == False):
                    dN[v] = prio + length
                    pq.put([dN[v], v, N])
                # But we cannot always jump
                elif(how == N and NJ == J and dJ[v] > prio + length and visited[v][NJ] == False):
                    dJ[v] = prio + length
                    pq.put([dJ[v], v, J])
    return None

Gr = [
    [0,1,0,0,0],
    [1,0,1,0,0],
    [0,1,0,7,0],
    [0,0,7,0,8],
    [0,0,0,8,0],
]
graph = [
            [0, 3, 0, 0, 0],
            [3, 0, 2, 0, 0],
            [0, 2, 0, 5, 0],
            [0, 0, 5, 0, 1],
            [0, 0, 0, 1, 0]
        ]
print(jumper(graph, 0, 4))