def find(v, parent):
    p = v
    while(p != parent[v]):
        p = parent[p]
    return p

def union(x, y, rang, parent):
    x = find(x, parent)
    y = find(y, parent)
    if(x == y):
        return
    if(rang[x] < rang[y]):
        parent[x] = y
    else:
        parent[y] = x
        if(rang[x] == rang[y]):
            rang[x] += 1

def MST(E, n):

    # Initialization:
    E.sort()
    A = [] # Subset of edges
    parent = [v for v in range(n)] # Not a graph parent, but MSC parent
    rang = [0 for _ in range(n)]

    # Main loop:
    for w, v, u in E:
        if(find(v, parent) != find(u, parent)): # It means adding the e edge to A will not create a cycle
            union(v, u, parent, rang)
            A.append((v, u))
    return A
