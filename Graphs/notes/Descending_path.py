# Task: find a path from a to b, that goes only on
# edges with descending weights

# Idea: we can use Djikstra with some modification in relaxation() function
# Sort all edges by length, do relaxation, go for it

from queue import PriorityQueue
def SortSecond(v):
    return v[1]

def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    pq = PriorityQueue()
    pq.put((0, s, float("inf"), [s])) # path_length, vertex_num, incoming edge, path

    # Pre-process:
    # For every vertex, we will sort outgoing edges in ascending order
    for v in range(n):
        G[v].sort(key=SortSecond)

    # Main loop:
    while (not pq.empty()):
        length, vertex, incom, path = pq.get()
        if(vertex == end):
            return path, length
        # Relaxation for the poped vertexes children:
        for (v, edge_len) in G[vertex]:
            if(edge_len > incom):
                continue # We cannot go this way
            pq.put((length+edge_len, v, edge_len, path+[v]))
    return None

G = [
    [(1, 2), (4, 2)],
    [(0, 2), (2, 3), (4, 1), (5, 1)],
    [(1, 3), (3, 1)],
    [(2, 1), (4, 5), (5, 1)],
    [(0, 2), (1, 1), (3, 5)],
    [(1, 8), (3, 1)]
]
G2 = [
    [(1, 5), (2, 1)],       # 0
    [(3, 4)],               # 1
    [(3, 1)],               # 2
    [(4, 3)],               # 3
    []                      # 4
]
start = 0
end = 4

print(dijkstra(G2, start, end))