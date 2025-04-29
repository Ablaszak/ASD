from collections import deque

def Dijkstra(G, s):
    # Init:
    q = deque()
    put = q.append
    get = q.popleft
    put(s)

    n = len(G)
    d = [float("inf") for _ in range(n)] # Distance from s to vertex