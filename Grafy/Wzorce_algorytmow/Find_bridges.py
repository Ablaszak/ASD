# DFS based algorithm finding bridges between parts of graph

def low_fun(G, v):
    global parent
    global time_arr
    global low_arr
    low = time_arr[v]
    for child in G[v]:
        if(child != parent[v]):
            if(low_arr[child] is not None):
                low = min(low, low_arr[child])
            elif(time_arr[child] is not None): # Traceback edge
                low = min(low, time_arr[child])
    if(low == time_arr[v] and time_arr[v] != 0): # Isn't a starting vertex (have to check this one seperately
        global bridge_counter
        bridge_counter += 1
    return low

def DFS_visit(G, v):
    #print("Entering vertex ", v)
    global parent
    global visited
    global time_arr
    global time
    time += 1
    # Visiting the v vertex:
    visited[v] = True
    time_arr[v] = time
    # Visiting neighbours:
    for n in G[v]:
        if(visited[n] == False):
            parent[n] = v
            DFS_visit(G, n)
    # The v vertex has been fully processed, we cann assign low value
    global low_arr
    low_arr[v] = low_fun(G, v)
    #print("Processed vertex ", v, low_arr[v])

def DFS(G):
    global visited
    for v in range(len(G)):
        if(visited[v] == False):
            DFS_visit(G, v)

# Undirected graph:
adj = [
    [1, 6],
    [0, 2],
    [1, 3, 6],
    [2, 4, 5],
    [3, 5],
    [3, 4],
    [0, 2, 7],
    [6]
]

n = len(adj)
time_arr = [None for _ in range(n)] # Time of visit of every vertex
time = -1 # Current time, goes up on every visit
low_arr = [None for _ in range(n)]
visited = [False for _ in range(n)]
parent = [None for _ in range(n)]
bridge_counter = 0

DFS(adj)
print(bridge_counter)
#print(low_arr)
#print(low_fun(adj, 5))