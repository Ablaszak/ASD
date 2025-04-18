# Algorithm finding strongly connected components in directed graph
# Def.: Two vertexes (u and v) are strongly connected <=>
#       There is a directed path from u to v and from v to u

def DFS_visit(G, v, final=False):
    if(final == True):
        global comp
        comp.append(v)
    global parent
    global visited
    global time
    global proc_t
    visited[v] = True
    #time += 1 # Visit time
    # Visiting neighbours:
    for n in G[v]:
        if(visited[n] == False):
            DFS_visit(G, n, final)
    proc_t[len(G)-1-time] = v
    time += 1 # Process time


def DFS(G):
    global visited
    for v in range(len(G)):
        if(visited[v] == False):
            DFS_visit(G, v)

def DFS_by_time(G):
    global visited
    global comp
    for v in proc_t:
        if(visited[v] == False):
            DFS_visit(G, v ,True)
            if(len(comp) > 1): # Added this to avoid considering single vertexes as connected components
                print(comp)
            comp = []

def rev_edges(G):
    global n
    rev = [[] for _ in range(n)]
    for v in range(n):
        for e in G[v]:
            rev[e].append(v)
    return rev

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
print(proc_t)
for i in range(n):
    visited[i] = False

adj = rev_edges(adj)
DFS_by_time(adj)
