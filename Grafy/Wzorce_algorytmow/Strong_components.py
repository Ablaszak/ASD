# Algorithm finding strongly connected components in directed graph
# Def.: Two vertexes (u and v) are strongly connected <=>
#       There is a directed path from u to v and from v to u


# 1st DFS phase:
def DFS_visit(G, v):
    global visited
    global time
    global proc_t
    visited[v] = True
    # Visiting neighbours:
    for n in G[v]:
        if(visited[n] == False):
            DFS_visit(G, n)
    proc_t[len(G)-1-time] = v
    time += 1 # Process time


def DFS(G):
    global visited
    for v in range(len(G)):
        if(visited[v] == False):
            DFS_visit(G, v)

# Middle DFS phase:
def rev_edges(G):
    n = len(G)
    rev = [[] for _ in range(n)]
    for v in range(n):
        for e in G[v]:
            rev[e].append(v)
    return rev

# 2nd FDS phase:
def DFS_run_components(G, v):
    global visited
    global comp
    comp.append(v)
    visited[v] = True
    # Visiting neighbours:
    for n in G[v]:
        if(visited[n] == False):
            DFS_run_components(G, n)

def DFS_by_time(G):
    global visited
    global comp
    for v in proc_t:
        if(visited[v] == False):
            DFS_run_components(G, v)
            if(len(comp) > 1): # Added this to avoid considering single vertexes as connected components
                print(comp)
            comp = []


# Directed graph:
adj2 = [
    [1, 2],
    [7],
    [3, 5],
    [4],
    [],
    [6, 7],
    [],
    [1, 2],
    []
]
# Another directed graph:
adj = [
    [1],        # 0
    [2],        # 1
    [0, 3],     # 2
    [4],        # 3
    [5, 6],     # 4
    [3],        # 5
    [7],        # 6
    [8],        # 7
    [6, 9],     # 8
    [10],       # 9
    [11],       #10
    [9, 12],    #11
    [13],       #12
    []          #13
]


n = len(adj)
time = 0
visited = [False for _ in range(n)]
proc_t = [None for _ in range(n)] # Time of processing a vertex
comp = []

# The main Algorithm:
DFS(adj)
#print(proc_t)
for i in range(n):
    visited[i] = False

adj = rev_edges(adj)
DFS_by_time(adj)
