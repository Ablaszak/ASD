"""
Bajtocja to bardzo bogaty kraj. Pracują w niej inżynierowie z całego świata. Niestety, rodzi to
czasem problemy. Okazuje się na przykład, że część linii kolejowych w Bajtocji ma indyjski rozstaw
szyn (1676 mm) a reszta ma rozstaw przylądkowy (1067 mm). Główny Rozkładowy, inżynier Armin
Mos, ma za zadanie zaplanować najkrótszą trasę ze stacji A do stacji B. Po drodze pociąg będzie
potencjalnie musiał przejechać przez pewne inne stacje. Jeśli pociąg wjeżdża na stację i wyjeżdża z
niej linią indyjską to przejazd zajmuje 5 jednostek czasu. Wjazd i wyjazd linią przylądkową zajmuje
10 jednostek czasu. Jeśli natomiast na stacji trzeba zmienić rozstaw kół to przejazd zajmuje 20
jednostek czasu. Pomiędzy stacjami pociąg jedzie z prędkością jednego kilometra na jednostkę
czasu. Odległości pomiędzy stacjami to dodatnie liczby naturalne nie większe niż 10 kilometrów.
Ruszając ze stacji A pociąg ma dopasowany rozkład kół do pierwszej linii, którą się porusza.
Proszę zaimplementować funkcję tory_amos(E, A, B), która otrzymuje na wejściu opis linii
kolejowych E, numer stacji początkowej A oraz numer stacji końcowej B i zwraca najkrótszy możliwy
czas przejazdu z A do B. Opis linii kolejowych to lista krotek postaci (x, y, d, typ), gdzie x i y
to numery stacji połączonych linią kolejową, d ∈ {1, …, 10} to długość linii zaś typ to jej rozstaw.
Jeśli typ == 'I' to linia ma rozstaw indyjski. Jeśli typ == 'P' to linia ma rozstaw przylądkowy.
Każda linia kolejowa jest dwukierunkowa (ma tor w kierunku x->y i tor w kierunku y->x). Może
się zdarzyć, że pewne stacje są połączone zarówno linią indyjską jak i linią przylądkową. Stacje
numerowane są od 0.
"""

from egz2btesty import runtests
from queue import PriorityQueue

def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    d = [[float("inf"), float("inf")] for _ in range(n)] # I income, P income
    parent = [[None, None] for _ in range(n)]
    d[s] = [0, 0] # <--- Very important, without this the algorithm won't start
    pq = PriorityQueue()
    pq.put((d[s][0], s, 0))
    pq.put((d[s][1], s, 1))
    
    # Main loop:
    while(not pq.empty()):
        prio, vertex, income = pq.get()
        if(vertex == end):
            for i in range(n):
                print(parent[i], d[i])
            #return prio
        if(prio <= d[vertex][income]): # We check the vertex only if we haven't already found a better path
            # Relaxation for the newly found vertex:
            for (v, length, excome) in G[vertex]:
                # same type of line:
                if(vertex == s):
                    time = 0
                elif(income == excome):
                    time = 5 + income*5
                # different types:
                else:
                    time = 20
                if(d[v][excome] > d[vertex][income] + length + time):
                    d[v][excome] = d[vertex][income] + length + time
                    parent[v][excome] = vertex
                    pq.put((d[v][excome], v, excome))
    return min(d[end])

def build_graph(E):
    n = 0
    for x, y, _, _ in E:
        n = max(n, x, y)
    n += 1
    G = [[] for _ in range(n)]
    for x, y, d, typ in E:
        if(typ == 'I'):
            G[x].append([y, d, 0])
            G[y].append([x, d, 0])
        else:
            G[x].append([y, d, 1])
            G[y].append([x, d, 1])
    
    return G

def tory_amos( E, A, B ):
    return dijkstra(build_graph(E), A, B)

runtests( tory_amos, all_tests = True )
