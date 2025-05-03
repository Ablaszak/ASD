#Simple BFS, storing parents and distances from the vertex globally

from collections import deque


def longer(G, s, t):
    size = len(G)
    visited = [False for _ in range(size)]
    d = [0 for _ in range(size)]  # distance
    parent = [[] for _ in range(size)] # Will help to find dead ends
    path_length = [0 for _ in range(size)] # Length of path going through i vertex
    def BFS(v):
        q = deque()
        put = q.append
        get = q.popleft
        put(v)
        nonlocal visited
        nonlocal d
        nonlocal parent
        path_exists = False
        while q:
            v = get()
            # Exploring neighboring vertices:
            for n in G[v]:
                if(n == t):
                    path_exists = True
                if(visited[n] == False):
                    # Updating the queue
                    parent[n].append(v)
                    visited[n] =  True
                    d[n] = d[v] + 1
                    # Simulating the wave advancing to the next vertex:
                    put(n)
        return path_exists

    # BFS from s to t
    if(BFS(s) == False):
        return None

    # Storing time of visits:
    for i in range(size):
        path_length[i] = d[i]
        d[i] = 0

    # Reset visited[] array
    for i in range(size):
        visited[i] = False

    # BFS from t to s
    BFS(t)

    # Counting sum of times
    for i in range(size):
        path_length += d[i]

    # Now we have to find the shortest path (smallest d[v])
    # and look for detours (bigger d[v])
    def find_parent(v): # We will use this function to find parent of two equally long paths (we won't be checking them)
        nonlocal path_counter
        path_counter = 0
        scout = []
        for i in G[v]:
            if(path_length[i] == path_length[v] and i != parent[v][1]):
                scout.append(i)
        for sc in scout:
            path_coutner = 0
            for i in G[sc]:
                if(path_length[i] == path_length[sc]):
                    path

    path_counter = 0 # Will help to find out if tere's more than one shortest path to a vertex
    v = t
    while(v != s):
        path_counter = 0
        for n in G[v]:
            if(path_length[n] == path_length[v]):
                path_counter += 1
            if(path_counter >= 2):
                v = find_parent(v)
                break



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


