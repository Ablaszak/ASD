# Podstawowy, "goły" DFS do modyfikowania na potrzeby zadań

def DFS_visit(G, v):
    global parent
    global visited
    global time
    visited[v] = True
    time += 1 # Czas odwiedzenia
    # Odwiedzanie sąsiadów:

    for n in G[v]:
        if(visited[n] == False):
            parent[n] = v
            DFS_visit(G, n)
    time += 1 # czas przetworzenia


def DFS(G):
    global visited
    for v in range(len(G)):
        if(visited[v] == False):
            DFS_visit(G, v)

# Graf skierowany:
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
time = 0
visited = [False for _ in range(n)]
parent = [None for _ in range(n)]

DFS(adj)

