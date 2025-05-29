from queue import PriorityQueue

def dijkstra(G, s, resorts):
    # Initialization:
    n = len(G)
    d = [float("inf") for _ in range(n)]
    d[s] = 0 # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]

    parent = [None for _ in range(n)]
    pq = PriorityQueue()
    pq.put((d[s], s))

    # Main loops:
    while(not pq.empty()):
        prio, vertex = pq.get()
        if(prio <= d[vertex]): # We check the vertex only if we haven't already found a better path
            visited[vertex] = True
            # Relaxation for the newly found vertex:
            for (v, length) in G[vertex]:
                if(d[v] > d[vertex] + length and visited[v] == False):
                    d[v] = d[vertex] + length
                    parent[v] = vertex
                    if(v not in resorts): # we won't use it to travel fusrther
                        pq.put((d[v], v))
    return d

def rewrite(E):
    n = max(max(u, v) for u, v, _ in E) + 1
    G = [[] for _ in range(n)]
    for u, v, w in E:
        G[u].append([v, w])
        G[v].append([u, w])
    return G, n

def lets_roll(start, G, resorts):
    G, n = rewrite(G)
    cost = 0
    d = dijkstra(G, start, resorts)
    for r in resorts:
        if(d[r] != float("inf")):
            cost += (d[r] * 2)
    return cost

inf = float("inf")
G=[
    (0,1,2),(0,2,4),(0,3,8),(3,4,16),(1,4,1),(2,4,1)
]
res = [1, 2, 4]

print(lets_roll(0, G, res))