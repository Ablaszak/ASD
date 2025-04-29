"""
Transitive closure

If we can go from vertex A to vertex B, and from B to C, we can go from A to C.

Transitive closure is an operation of creating additional edges between
vertexes we can traverse between (and are not adjacent, because in such
case we already have an edge)
"""

# Directed graph with no additional transitive edges:
G = [
    [0,1,0,1,1,1,1],
    [0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,1,0,0,1,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1]
]

# After creating transitive edges (marked as '2'):
G2 = [
    [0, 1, 2, 1, 1, 1, 1],
    [0, 2, 1, 2, 2, 0, 0],
    [0, 2, 2, 1, 2, 0, 0],
    [0, 1, 2, 2, 1, 0, 0],
    [0, 2, 1, 2, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 1]
]

# Rozwiązanie:
def domk(M):
    n = len(M)
    for u in range(n):
        for src in range(n):
            for target in range(n):
                if(M[src][u] != 0 and M[u][target] != 0 and M[src][target] == 0): # Last condition is not necessery, but it will allow us not to override value 1 with 2
                    M[src][target] = 2
    return M

domk(G)
for i in range(len(G)):
    print(G[i])
