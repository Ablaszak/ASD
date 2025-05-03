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
# Number of vertices:
#v = 5

# Adjacency list:
adj = [

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