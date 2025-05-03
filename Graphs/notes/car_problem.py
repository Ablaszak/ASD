D = 5 # Fuel tank capacity
# Problem: We have to navigate a car from start do end on a graph with marked vertexes with gas stations
# Idea: We create a new graph including only vertexes and edges we can reach and travel through (including gas stations)
# Implementation: To do

G = [
    [(1, 4), (2, 2)],
    [(3, 2)],
    [(3, 3), (4, 1)],
    [(2, 3), (4, 1)],
    [(5, 2), (6, 2), (7, 3)],
    [(1, 0), (8, 1)],
    [(8, 2)],
    [(9, 3)],
    [(9, 5)]
    ]

t = True
f = False
Stations = [t,f,f,t,f,f,f,f,t,f]

from queue import PriorityQueue

def dijkstra(G, s, end):
    # Initialization:
    global Stations
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[s] = 0 # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, D, [s])) # Path_length, vertex, Fuel_on_entry, path

    # Main loop:
    while(not pq.empty()):
        prio, vertex, incom, path = pq.get()
        if(vertex == end):
            return parent
        # Relaxation for the newly found vertex:
        for (v, length) in G[vertex]:
            if(length > incom):
                continue # we cannot go this way
            # Now we actually check adjacent vertex:
            if(Stations[v] == True):
                pq.put((prio + length, v, D, path+[v]))
            else:
                pq.put((prio + length, v, (incom-length), path + [v]))
    return None

