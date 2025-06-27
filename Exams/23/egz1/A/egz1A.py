"""
Złycerz (czyli zły rycerz) wędruje po średniowiecznym grafie G = (V, E), gdzie waga każdej
krawędzi to liczba sztabek złota, którą trzeba zapłacić za przejazd nią (myta, jedzenie, itp.). W
każdym wierzchołku znajduje się zamek, który zawiera w skarbcu pewną daną liczbę sztabek
złota. Złycerz może napaść na jeden zamek i zabrać całe jego złoto, ale od tego momentu
zaczyna być ścigany i każdy przejazd po krawędzi jest dwa razy droższy, oraz dodatkowo na
każdej drodze musi zapłacić r sztabek złota jako łapówkę (zatem od tej pory koszt przejazdu
danej krawędzi jest równy dwukrotności wagi tej krawędzi plus wartość r). Co więcej, Złycerz nie
może napaść więcej niż jednego zamku, bo jest trochę leniwy (oprócz tego, że zły). Proszę wskazać trasę Złycerza z zamku s do t o najmniejszym koszcie (lub największym zysku, jeśli to możliwe).
Uwaga. Złycerz może przejechać po danej krawędzi więcej niż raz (np. raz jadąc do zamku, który
chce napaść, a potem z niego wracając).
Zadanie polega na implementacji funkcji:
gold( G,V,s,t,r ),
która na wejściu otrzymuje: graf G reprezentowany w postaci listowej, tablicę V zawierającą liczby
sztabek złota w kolejnych zamkach, zamek początkowy s, zamek końcowy t oraz wysokość łapówki r.
Funkcja powinna zwrócić najmniejszy koszt drogi uwzględniający ewentualny napad. Jeżeli zysk
z napadu jest większy, od kosztu drogi należy, powstały zysk należy zwrócić jako liczbę ujemną
"""

from egz1Atesty import runtests
from queue import PriorityQueue

def dijkstra(G, V, s, end, r):
    # Initialization:
    n = len(G)
    parent1 = [None for _ in range(n)]
    d1 = [float("inf") for _ in range(n)] # Before robbing a castle
    d2 = [float("inf") for _ in range(n)] # After robbing a castle
    d1[s] = 0 # <--- Very important, without this the algorithm won't start
    d2[s] = -V[s]
    visited1 = [False for _ in range(n)]
    visited2 = [False for _ in range(n)]
    pq = PriorityQueue()
    pq.put((d1[s], s, 0)) # total cost, current vertex, did rob?
    pq.put((d2[s], s, 1))

    # Main loop:
    while(not pq.empty()):
        prio, vertex, rob = pq.get()
        #if(vertex == end):
        #    return prio
        # Haven't robbed (yet >:3):
        if(rob == 0):
            if(prio <= d1[vertex]): # We check the vertex only if we haven't already found a better path
                visited1[vertex] = True
                # Relaxation for the newly found vertex:
                for (v, length) in G[vertex]:
                    # Not robbing:
                    if(d1[v] > d1[vertex] + length ):
                        d1[v] = d1[vertex] + length
                        parent1[v] = vertex
                        pq.put((d1[v], v, 0))
                    # Robbing current castle:
                    if(d2[v] > d1[vertex] + 2*length + r - V[vertex]):
                        d2[v] = d1[vertex] + 2*length + r - V[vertex]
                        pq.put((d2[v], v, 1))
        # Have robbed:
        if(rob == 1):
            if(prio <= d2[vertex]):
                visited2[vertex] = True
                for(v, length) in G[vertex]:
                    if(d2[v] > (d2[vertex] + 2*length + r) ):
                        d2[v] = d2[vertex] + 2*length + r
                        pq.put((d2[v], v, 1))
    return min(d1[end], d2[end])

def gold(G,V,s,t,r):
    return dijkstra(G, V, s, t, r)

runtests( gold, all_tests = True )
