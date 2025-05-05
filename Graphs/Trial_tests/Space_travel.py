"""
Układ planetarny Algon składa się z n planet o numerach od O do n - l. Niestety własności
fizyczne układu powodują, że nie da się łatwo przelecieć między dowolnymi dwiema planetami. Na
szczęście mozolna eksploracja kosmosu doprowadziła do stworzenia listy E dopuszczalnych bezpośrednich przelotów. Każdy element listy E to trójka postaci ( u, v, t), gdzie u i v to numery planet
(można założyć, że u < v) at to czas podróży między nimi (przelot z u do v trwa tyle samo co
z v do u). Dodatkową nietypową własnością układu Algon jest to, że niektóre planety znajdują
się w okolicy osobliwości. Znajdując się przy takiej planecie możliwe jest zagięcie czasoprzestrzeni
umożliwiające przedostanie się do dowolnej innej planety leżącej przy osobliwości w czasie zerowym.
Zadanie polega na zaimplementowaniu funkcji:
def spacetravel( n, E, S, a, b)
która zwraca najkrótszy czas podróży z planety a do planety b, mając do dyspozycji listę możliwych
bezpośrednich przelotów E oraz listę S planet znajdujących się koło osobliwości. Jeśli trasa nie
istnieje, to funkcja powinna zwrócić None.
Rozważmy następujące dane:
E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ o, 2, 3 ]
a = 1
b = 5
n = 7
1
wywołanie startravel(n, E, S, a, b) powinno zwrócić liczbę 13. Odwiedzamy po kolei planety
1, 3, 2, 4, 6 i kończymy na planecie 5 (z planety 2 do 3 dostajemy się przez zagięcie czasoprzestrzeni).
Gdyby a= l ab= 2 to wynikiem byłby czas przelotu 1.
"""

from queue import PriorityQueue

def prepare(edge, n, S, start,  end):
    graph = [[] for _ in range(n+1)] # +1 is for singularities
    for u, v, t in edge:
        if(u in S):
            graph[n].append([v, t])
            graph[v].append([n, t])
        else:
            if(v in S):
                graph[n].append([u, t])
                graph[u].append([n, t])
            else:
                graph[u].append([v, t])
                graph[v].append([u, t])
    if(end in S):
        end = n
    if(start in S):
        start = n
    return graph, start, end


def startravel(n, edge, S, s, end):
    # Initialization:
    edge, s, end = prepare(edge, n, S, s, end)
    n = len(edge)
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[s] = 0 # <--- Very important, without this the algorithm won't start
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    pq.put((d[s], s))

    # Main loop:
    while(not pq.empty()):
        prio, vertex = pq.get()
        if(vertex == end):
            print(parent)
            return prio
        if(prio <= d[vertex]): # We check the vertex only if we haven't already found a better path
            visited[vertex] = True
            # Relaxation for the newly found vertex:
            for (v, length) in edge[vertex]:
                if(d[v] > d[vertex] + length and visited[v] == False):
                    d[v] = d[vertex] + length
                    parent[v] = vertex
                    pq.put((d[v], v))
    return None

inf = float("inf")

start = 0
dest = 5
E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]

print(startravel(7, E, S, 0, 3))