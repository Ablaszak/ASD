from collections import deque

def Dijkstra(G, s):
    # ----------------- INIT -----------------
    # Queue:
    q = deque()
    put = q.append
    get = q.popleft
    put(s)

    n = len(G)

    # Arrays:
    d = [float("inf") for _ in range(n)] # Distance from s to all vertexes
    d[s] = 0
    visited = [False for _ in range(n)]
    visited[s] = True
    put(s)

    # -------------- MAIN LOOP --------------
    while(True)


