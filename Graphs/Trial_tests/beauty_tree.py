"""
Dany jest ważony, nieskierowany graf G = (V, E), którego wagi krawędzi opisuje funkcja w∶ E → N.
Wiadomo, że wagi krawędzi są parami różne. Niech T będzie pewnym drzewem rozpinającym G,
m będzie najmniejszą wagą krawędzi z T a M będzie największą wagą krawędzi z T. Mówimy, że
T jest piękne jeśli każda krawędź spoza T albo ma wagę mniejszą niż m albo większą niż M. Wagą
drzewa rozpinającego jest suma wag jego krawędzi. Zadanie polega na implementacji funkcji:
beautree( G )
która na wejściu otrzymuje graf reprezentowany w postaci listowej i zwraca wagę najlżejszego pięknego drzewa rozpinającego G lub None jeśli takie drzewo nie istnieje. Użyty algorytm powinien być
możliwie jak najszybszy. Proszę uzasadnić poprawność zaproponowanego algorytmu oraz oszacować
jego złożoność czasową i pamięciową.
"""

def rewrite(G):
    E = []
    n = len(G)
    for u in range(n):
        for v, w in G[u]:
            if(u<v):
                E.append( (w, u, v) )
    E.sort()
    return E

def find(v, parent):
    p = v
    if(p != parent[p]):
        parent[p] = find(parent[p], parent)
    return parent[p]

def union(x, y, parent, rank):
    x = find(x, parent)
    y = find(y, parent)
    if(x == y):
        return
    if(rank[x] < rank[y]):
        parent[x] = y
    else:
        parent[y] = x
        if(rank[x] == rank[y]):
            rank[x] += 1

def beautree(G):
    V = len(G)
    G = rewrite(G)
    E = len(G)
    if(E < V-1):
        return None
    for i in range(E - (V)):
        skip = False
        W = 0
        rank= [1 for _ in range(V)]
        parent = [v for v in range(V)]
        for j in range(V-1):
            w, v, u = G[i+j]
            if(find(v, parent) == find(u, parent)):
                skip = True
                break
            W += w
            union(v, u, parent, rank)
        if(skip == False):
            return W
    return None


Graph = [ [(1,3), (2,1), (4,2)], # 0
[(0,3), (2,5) ], # 1
[(1,5), (0,1), (3,6)], # 2
[(2,6), (4,4) ], # 3
[(3,4), (0,2) ] ] # 4

print(beautree(Graph))