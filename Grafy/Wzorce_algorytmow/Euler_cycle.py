# Finding Euler cycle in undirected graph using DFS
# We assume that such cycle exists in given graph

def DFS_visit(G, v):
    global parent
    global V
    global it

    # Deleting parent edge before processing given vertex:
    if(parent[v] is not None):
        for e in range(len(G[parent[v]])):
            if(G[parent[v]][e] == v):
                G[parent[v]][e] = None
                break
        for e in range(len(G[v])):
            if(G[v][e] == parent[v]):
                G[v][e] = None
                break

    # Visiting neighbours:
    for n in range(len(G[v])):
        if(G[v][n] is not None):
            parent[n] = v
            DFS_visit(G, n)

    # Adding v to output array:
    V[it] = v
    it -= 1


# Undirected graph:
adj = [
    [1, 2],
    [0, 3],
    [0, 3, 4, 5],
    [1, 2, 4, 5],
    [2, 3],
    [2, 3]
]

n = len(adj)
visited = [False for _ in range(n)]
parent = [None for _ in range(n)]

# Counting edges:
E = 0
for i in range(n):
    E += len(adj[i])

V = [None for _ in range(E)] # Output array
it = (E//2)-1 # V iterator
DFS_visit(adj, 0)
print(V)
