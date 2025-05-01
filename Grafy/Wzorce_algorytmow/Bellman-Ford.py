
def B_F(G, s):

    # Initialization:
    n = len(G)
    d = [float("inf") for _ in range(n)]
    d[s] = 0
    parent = [None for _ in range(n)]

    # Main loop:
    for i in range(n - 1):
        # Relax:
        for (v, e) in G[i]:
            if(d[v] > d[i] + e):
                d[v] = d[i] + e
                parent[v] = i

    # Check for negative cycles:
    for i in range(n - 1):
        # Relax:
        for (v, e) in G[i]:
            if(d[v] > d[i] + e):
                return -1
    return parent

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
path = B_F(G, start)

while(end != start):
    print(end, end=" <--- ")
    end = path[end]
print(end)