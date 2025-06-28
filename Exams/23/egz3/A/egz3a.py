"""
Dobrycerz (czyli rycerz, który zawsze uprzejmie mówi “dzień dobry”) chce się przedostać z zamku s
do zamku t. Mapa zamków dana jest w postaci grafu nieskierowanego G, gdzie każda krawędź ma wagę oznaczającą ile godzin potrzeba, żeby ją przebyć. Wagi to liczby naturalne ze zbioru {1, 2, . . . , 8}.
Po najdalej 16 godzinach podróży Dobrycerz musi nocować w zamku. Warunki uprzejmości wymagają, żeby spędził w takim zamku 8 godzin (przejazd przez zamki, w których nie nocuje nie
kosztuje dodatkowego czasu; szybko mówi “dzień dobry” strażnikom i jedzie dalej). Mapa z której
korzysta Dobrycerz ma to do siebie, że liczba dróg jest proporcjonalna do liczby zamków. Czyli jeśli
zamków jest n, to wiadomo, że dróg jest O(n).
Zadanie polega na implementacji funkcji:
goodknight( G, s, t )
która na wejściu otrzymuje graf opisujący mapę zamków, reprezentowany w postaci macierzy sąsiedztwa (czyli G[i][j] to liczba godzin, konieczna do przejechania bezpośrednio z zamku i do
zamku j; w przypadku braku drogi G[i][j] = −1), zamek startowy s oraz zamek docelowy t, i
zwraca minimalny czas (wyrażony w godzinach) potrzebny na przejazd z s do t (Dobrycerz nigdy
nie musi nocować ani w zamku s ani w zamku t). Można założyć, że zawsze istnieje trasa z zamku
s do t.
"""

from egz3atesty import runtests
from queue import PriorityQueue

def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    parent = [None for _ in range(n)]
    # d is an array of time of arrival for every state,
    # where state is how much energy we have on entry
    d = [[float("inf") for _ in range(17)] for _ in range(n)]
    d[s][16] = 0 # <--- Very important, without this the algorithm won't start
    pq = PriorityQueue()
    pq.put((d[s][16], s, 16))

    # Main loop:
    while(not pq.empty()):
        prio, vertex, energy = pq.get()
        if(vertex == end):
            return prio
        if(prio <= d[vertex][energy]): # We check the vertex only if we haven't already found a better path
            # Travel without sleeping:
            for v in range(n):
                length = G[vertex][v]
                if(length != -1 and length <= energy): # road exists and is traversable
                    exhaustion = energy - length
                    if(d[v][exhaustion] > d[vertex][energy] + length):
                        d[v][exhaustion] = d[vertex][energy] + length
                        pq.put((d[v][exhaustion], v, exhaustion))
            # Go to sleep:
            if(energy != 16):
                if(d[vertex][16] > prio+8):
                    d[vertex][16] = prio + 8
                    pq.put((prio+8, vertex, 16))
    return None

def goodknight( G, s, t ):
    return dijkstra(G, s, t)

runtests( goodknight, all_tests = True )


