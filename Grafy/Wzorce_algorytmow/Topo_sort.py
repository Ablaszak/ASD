# Topo sorting algorithm using DFS

def DFS_visit(G, v):
    global visited
    global V
    global it
    visited[v] = True
    # Visiting neighbours:
    for n in G[v]:
        if(visited[n] == False):
            DFS_visit(G, n)
    # v vertex was just processed, we can add it to V array
    V[it] = v
    it -= 1


def DFS(G):
    global visited
    for v in range(len(G)):
        if(visited[v] == False):
            DFS_visit(G, v)

# directed graph:
adj = [
    [1, 2],
    [8],
    [3, 5],
    [4],
    [],
    [6, 8],
    [],
    [],
    [7]
]

n = len(adj)
visited = [False for _ in range(n)]
# output array for sorted vertices:
V = [0 for _ in range(n)]
it = n-1 # Global V array iterator
DFS(adj)
print(V)

