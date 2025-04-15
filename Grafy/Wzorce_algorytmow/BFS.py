"""
Prosty BFS, zapisujący parentów i odległości od wierzchołka globalnie
"""

from collections import deque

def BFS(adj, s=0):
    q = deque()
    put = q.append
    get = q.popleft
    put(s) # domyślnie 0
    global visited
    global parent
    global d
    while q:
        v = get()
        # Przeglądanie sąsiednich wierzchołków:
        for n in adj[v]:
            if(visited[n] == False):
                # Aktualizacja kolejki
                visited[n] = True
                parent[n] = v
                d[n] = d[v] + 1
                # Symulacja postępowania fali do następnego wierzchołka:
                put(n)




# Zakładamy graf nieskierowany
# Liczba wierzchołków:
#v = 5

# Lista sąsiedztwa:
adj = [[1, 3, 4], [0, 2, 3], [1], [0, 1, 4], [0, 3]]
adj2 = [
    [1, 2],        # 0 sąsiaduje z 1 i 2
    [0, 3, 4, 5],  # 1 sąsiaduje z 0, 3, 4, 5
    [0, 5],        # 2 sąsiaduje z 0, 5
    [1],           # 3 sąsiaduje z 1
    [1, 5, 6],     # 4 sąsiaduje z 1, 5, 6
    [1, 2, 4, 7],  # 5 sąsiaduje z 1, 2, 4, 7
    [4, 7],        # 6 sąsiaduje z 4, 7
    [5, 6]         # 7 sąsiaduje z 5, 6
]
n = len(adj2)
visited = [False for _ in range(n)]
d = [0 for _ in range(n)] # odległość
parent = [None for _ in range(n)]

BFS(adj2)
# Próbne znalezienie najkrótszej ścieżki od 0 do 7:
v = 7
print(v, end="")
while(v != 0):
    v = parent[v]
    print(" <-- ", v, end="")

"""
q = deque()
put = q.append
get = q.popleft
put(123)
"""