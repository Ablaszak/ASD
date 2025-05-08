def directed_graph(G):
    """
    We count distance between every two vertexes using Floyd-Warshall.
    Then we count cycle length = d(v, u) + d(u, v) and choose minimal
    """

    # Floyd - Warshall:
    n = len(G)
    for shortcut in range(n):
        for v in range(n):
            for u in range(n):
                G[u][v] = min(G[u][v], G[u][shortcut] + G[shortcut][v])

    cycle = float("inf")
    for v in range(n):
        for u in range(v):
            if(G[u][v] != float("inf") and G[v][u] != float("inf")):
                cycle = min(cycle, G[v][u] + G[u][v])
    return cycle

from queue import PriorityQueue
def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    d = [float("inf") for _ in range(n)]
    d[s] = 0 # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    pq.put((d[s], s))

    finish = False
    # Main loop:
    while(not pq.empty()):
        prio, vertex = pq.get()
        if(vertex == end and finish):
            return prio
        finish = True
        if(prio <= d[vertex]): # We check the vertex only if we haven't already found a better path
            visited[vertex] = True
            # Relaxation for the newly found vertex:
            for v in range(n):
                length = G[vertex][v]
                if(d[v] > d[vertex] + length and visited[v] == False):
                    d[v] = d[vertex] + length
                    pq.put((d[v], v))
    return float("inf")

def undirected_graph(G):
    """
    We are going to use edge removal and dijkstra for every vertex
    """
    n = len(G)
    cycle = float("inf")
    for v in range(n):
        for u in range(v):
            # temp edge removal:
            e = G[u][v]
            G[u][v] = float("inf")
            G[v][u] = float("inf")
            # Run Dijkstra:
            cycle = min(cycle, dijkstra(G, v, u) + e)
            # Bring back deleted edge:
            G[u][v] = e
            G[v][u] = e
    return cycle

INF = float("inf")
UGr = [
    [0, 4, INF, 5, INF],
    [INF, 0, 1, INF, 6],
    [2, INF, 0, 3, INF],
    [INF, INF, INF, 0, 2],
    [1, INF, INF, INF, 0]
]
DGr =  [
    [INF, 3, INF, 2, INF],
    [3, INF, 8, INF, 5],
    [INF, 8, INF, INF, 3],
    [2, INF, INF, INF, 2],
    [INF, 5, 3, 2, INF]
]

print(undirected_graph(DGr))