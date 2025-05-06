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

def MST(E, n):

    # Initialization:
    A = [] # Subset of edges
    parent = [v for v in range(n)] # Not a graph parent, but MSC parent
    rank= [0 for _ in range(n)]

    # Main loop:
    for w, v, u in E:
        if(find(v, parent) != find(u, parent)): # It means adding the e edge to A will not create a cycle
            union(v, u, parent, rank)
            A.append((v, u))
    return A

def beautree(G):
    V = len(G)
    G = rewrite(G)
    E = len(G)
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