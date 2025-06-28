"""
Duathlon na orientację polega na tym, że zawodnik najpierw biegnie ze startu 𝑠 do wybranego
przez siebie roweru (dowolnego z wielu dostępnych), a następnie jedzie na tym rowerze do mety
𝑡 (może też biec prosto do mety, nie biorąc roweru). Gdy zawodnik wybierze jakiś rower, to nie
może go już zmienić (ale nie musi w danym punkcie brać roweru, nawet jak jest dostępny). Luiza
Silnoręka startuje w takich zawodach i chce zaplanować to najszybsze pokonanie trasy. Trasa
reprezentowana jest jako graf ważony, w którym wierzchołki to punkty orientacyjne (wliczając w
to start 𝑠 i metę 𝑡) a krawędzie to ścieżki, którymi można się między tymi punktami poruszać.
Każda krawędź (ścieżka) ma czas wyrażony w minutach, jaki Luiza potrzebuje, żeby ją przebiec
(są to zawsze liczby naturalne). W każdym punkcie orientacyjnym może być jeden, kilka, lub zero
rowerów. Każdy rower opisany jest przez dwie liczby naturalne, 𝑝 i 𝑞. Wiadomo, że jeśli Luiza
potrzebuje 𝑥 minut aby przebyć pewną ścieżkę, to na rowerze opisanym przez 𝑝 i 𝑞 przejedzie ją
w czasie 𝑥*𝑝/𝑞 (o ile możnaby oczekiwać, że 𝑝 < 𝑞, to niektóre rowery są tak niewygodne, że ten
warunek nie zachodzi).
Proszę zaimplementować funkcję armstrong(B, G, s, t), która otrzymuje na wejściu listę 𝐵
opisującą dostępne rowery, graf 𝐺 opisujący trasę, oraz numery wierzchołków 𝑠 i 𝑡, a zwraca
najmniejszą liczbę minut (zaokrągloną w dół), jaką Luiza potrzebuje na pokonanie trasy duathlonu.
Lista 𝐵 zawiera trójki postaci (𝑖, 𝑝, 𝑞), gdzie 𝑖 to numer wierzchołka, w którym jest rower o
parametrach 𝑝 i 𝑞. W danym wierzchołku może być kilka rowerów i wówczas trójka z tą samą
wartością 𝑖 pojawia się w danych kilka razy.
Graf 𝐺 ma wierzchołki o numerach od 0 do 𝑛 − 1, jest nieskierowany i jest reprezentowany przez
listę krawędzi. Każda krawędź to trójka w postaci (𝑢, 𝑣, 𝑤), gdzie 𝑢 i 𝑣 to numery wierzchołków,
które łączy, a 𝑤 to liczba minut, przez którą Luiza przebiega tę krawędź.
"""

from egz1atesty import runtests
from queue import PriorityQueue

def dijkstra(G, s, end):
    # Initialization:
    n = len(G)
    df = [float("inf") for _ in range(n)]
    db = [float("inf") for _ in range(n)]
    df[s] = 0 # <--- Very important, without this the algorithm won't start

    pq = PriorityQueue()
    pq.put((df[s], s, 1))
    if(G[s][2] is not None): # start with a bike
        db[s] = 0
        pq.put(db[s], s, G[s][2])

    # Main loop:
    while(not pq.empty()):
        prio, vertex, bike_mod = pq.get()
        if(vertex == end):
            return int(prio)
        
        # We dont have a bike:
        if(bike_mod == 1 and prio <= df[vertex]): # We check the vertex only if we haven't already found a better path
            # Go further on foot:
            for (v, length, bike) in G[vertex]:
                if(df[v] > prio + length):
                    df[v] = prio + length
                    pq.put((df[v], v, 1))
            # Try taking a bike:
            if(G[vertex][2] is not None):
                pq.put((prio, vertex, G[vertex][2]))
        
        # Or we do have a bike:
        elif(prio <= db[vertex]):
            for(v, length, bike) in G[vertex]:
                length *= bike_mod
                if(db[v] > prio + length):
                    db[v] = prio + length
                    pq.put(db[v], v, bike_mod)
            
    return None

# O(n)
def build_graph(G, B):
    n = 0
    for u, v, _ in G:
        n = max(n, u, v)
    
    graph = [[] for _ in range(n)]
    for u, v, w in G: # O(n)
        graph[u].append([v, w, None]) # Last field is for bike
        graph[v].append([u, w, None])
    
    # Add bikes:
    for i, p ,q in B: # O(len(B)) ~ O(n)
        if(p/q >= 1): # useless bike
            continue
        
        if(graph[i][2] is None): # there is no bike
            graph[i][2] = p/q
        elif(p/q < graph[i][2]): # choose better bike
            graph[i][2] = p/q
        
    return graph
    
def armstrong(B, G, s, t):
    return dijkstra(build_graph(G, B), s, t)

runtests( armstrong, all_tests = False )