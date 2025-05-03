"""
find the shortest path between all vertexes
"""

INF = float("inf")
G = [
    [0, 4, INF, 5, INF],
    [INF, 0, 1, INF, 6],
    [2, INF, 0, 3, INF],
    [INF, INF, 1, 0, 2],
    [1, INF, INF, 4, 0]
]

def F_W(G):
    n = len(G)
    for shortcut in range(n):
        for v in range(n):
            for u in range(n):
                G[u][v] = min(G[u][v], G[u][shortcut] + G[shortcut][v])

for i in range(len(G)):
    print(G[i])

F_W(G)

print()
for i in range(len(G)):
    print(G[i])
