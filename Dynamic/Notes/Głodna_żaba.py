"""
A frog is sitting peacefully (this is important!) on field number 0.
There are n fields in total, numbered from 0 to n - 1.

The frog can jump any number of fields forward. However, each jump consumes a certain amount of energy, depending on the jump length.
Specifically, let C[i] represent the number of kilocalories (kcal) required to jump forward by i fields.
Some of the fields contain snacks.
Let A[i] be the number of kilocalories gained by eating the snack on field i.

Initially, the frog has 0 kcal of energy.

The goal:
Determine the minimum number of jumps the frog needs to reach field n - 1.

Constraints / Notes:

You can assume C[i] <= i².

The frog’s energy level can never drop below 0 at any point.

We assume frog can't jump backward
"""
"""
Pomysł:
Funkcja f(pole na którym jesteśmy, aktualna energia) = 
        = min liczba skoków potrzebna na dotarcie do tego pola
f(0, A[0]) = 0
f(0, cokolwiek inego) = inf 

f(i, e) = min( f(i-k, e-c[k]+przekąska) ) + 1; iterując k odpowiednio
Wynikiem jest 
minimum (iterując po energii bo musi być dowolna) ( f(n-1, e) )
Można ograniczyć energię do n**2, przy założeniu że po zjedzieniu
czegoś o energii >= n**2 skaczemy od razu na koniec
(wynika z warunków zadania)
"""

"""
Other idea:
build a graph and use dijkstra algorithm
"""

from queue import PriorityQueue

def dijkstra(A, C):
    # We assume C[0] = 0
    n = len(A)

    # Build graph:
    """
    graph is a list of lists of tuples:
    [cost of jump from i to j, vertex nr, snack value]
    """
    # lists init:
    G = [[] for i in range(n)]
    # Expand lists:
    for s in range(0, n): # Start
        for e in range(s+1, n): # End
            G[s].append((C[e], e, A[e]))

    # Initialization:
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[0] = 0 # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    pq.put((d[0], 0, A[0]))

    n -= 1 # Now it points at last vertex
    # Main loop:
    while(not pq.empty()):
        prio, vertex, energy = pq.get()
        if(vertex == n):
            return parent
        if(prio <= d[vertex]): # We check the vertex only if we haven't already found a better path
            visited[vertex] = True
            # Relaxation for the newly found vertex:
            for (v, length, edible) in G[vertex]:
                if(d[v] > d[vertex] + length and visited[v] == False and energy >= C[v - vertex]):
                    d[v] = d[vertex] + length
                    parent[v] = vertex
                    pq.put((d[v], v, energy-length+edible))
    return None

C = [0,5,5,2,78,1,2]
A = [5,5,0,10,0,5,0]

print(dijkstra(A, C))









