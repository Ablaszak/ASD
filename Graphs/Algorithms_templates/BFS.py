#Simple BFS, storing parents and distances from the vertex globally

from collections import deque

def BFS(adj, s=0):
    q = deque()
    put = q.append
    get = q.popleft
    put(s) # default is 0
    global visited
    global parent
    global d
    visited[s] = True
    while q:
        v = get()
        # Exploring neighboring vertices:
        for n in adj[v]:
            if(visited[n] == False):
                # Updating the queue
                visited[n] = True
                parent[n] = v
                d[n] = d[v] + 1
                # Simulating the wave advancing to the next vertex:
                put(n)


# Assuming an undirected graph

# Adjacency list:
adj = [[1, 3, 4], [0, 2, 3], [1], [0, 1, 4], [0, 3]]
adj2 = [
    [1, 2],        # 0 is adjacent to 1 and 2
    [0, 3, 4, 5],  # 1 is adjacent to 0, 3, 4, 5
    [0, 5],        # 2 is adjacent to 0, 5
    [1],           # 3 is adjacent to 1
    [1, 5, 6],     # 4 is adjacent to 1, 5, 6
    [1, 2, 4, 7],  # 5 is adjacent to 1, 2, 4, 7
    [4, 7],        # 6 is adjacent to 4, 7
    [5, 6]         # 7 is adjacent to 5, 6
]
n = len(adj2)
visited = [False for _ in range(n)]
d = [0 for _ in range(n)] # distance
parent = [None for _ in range(n)]

BFS(adj2)
# Trial: finding the shortest path from 0 to 7:
v = 7
print(v, end="")
while(v != 0):
    v = parent[v]
    print(" <-- ", v, end="")
