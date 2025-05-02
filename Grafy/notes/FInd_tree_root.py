# We have a tree
# We want to find vertex with the shortest distance to the most remote leaf
"""
Idea 1:
We can find two most remote leafs and
    a) check all vertexes in path between them
    b) or we can find a middle vertex by median
How to find two leafs:
    Start on a random vertex and count distance to all leafs
    Find the furthest leaf, if there's more than one, choose a random leaf (there are max 2 leafs)
    Run distance() function again, starting from a newly found leaf, find the furthest leaf from new start
    We now have the longest path between two leafs

"""

from collections import deque

def BFS(adj, s=0):
    q = deque()
    put = q.append
    get = q.popleft
    put(s) # default is 0
    n = len(adj)
    visited = [False for _ in range(n)]
    d = [0 for _ in range(n)] # distance
    parent = [None for _ in range(n)]
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
    return parent, d

G = [
    [1],
    [0, 2, 6],
    [1, 3],
    [2, 4],
    [3, 5],
    [4],
    [1, 7, 8],
    [6, 9],
    [6],
    [7, 10],
    [9]
]

start = 0
paths, d = BFS(G, start)
leaf1 = [0, 0]
for i in range(len(d)):
    if(d[i] > leaf1[1]):
        leaf1 = [i, d[i]]

# Now we look for a second leaf
paths, d = BFS(G, leaf1[0])

leaf2 = [0, 0]
for i in range(len(d)):
    if(d[i] > leaf2[1]):
        leaf2 = [i, d[i]]

# Only thing left is trace back (leaf2[1]) steps back from leaf2

root = leaf2[0]
for i in range(leaf2[1] // 2):
    root = paths[root]
print(root)