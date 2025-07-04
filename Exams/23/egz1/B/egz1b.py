"""
Przedstawiciel Gwiezdnej Floty podróżuje z planety A do planety B. Po drodze będzie musiał
wylądować na innych planetach w celu uzupełnienia paliwa. Cena paliwa na każdej planecie może
być inna. Dodatkowo na każdej planecie jest teleport, który może przenieść go na jedną z kolejnych
planet. Niestety, w tym celu jego statek kosmiczny musi mieć pusty zbiornik paliwa. Zaproponuj i
zaimplementuj algorytm, który oblicza minimalny koszt pokonania trasy z planety A do B.
Na trasie przedstawiciela Gwiezdnej Floty znajduje się n planet opisanych w tablicach D, C i T:
• D[i] to odległość i-tej planety od planety A wyrażona w latach świetlnych wzdłuż trasy
przelotu. Planety uporządkowane są w kolejności rosnącej odległości od A. Nie dopuszczamy
sytuacji, w której dwie planety mają tą samą odległość od A.
• C[i] to cena jednej tony paliwa na planecie numer i,
• T[i] to para postaci (j, p), gdzie j to numer planety, na którą można dostać się teleportem
z planety i (zawsze zachodzi j ≥ i, gdzie j = i oznacza, że teleport na tej planecie nie działa)
a p to cena skorzystania z teleportu.
Planeta A ma numer 0 a planeta B ma numer n − 1. Statek kosmiczny potrzebuje tony paliwa na
pokonanie każdego roku świetlnego. Pojemność zbiornika statku kosmicznego wynosi E ton. Nie
ma obowiązku tankowania paliwa do pełna. Zakładamy, że E oraz wszystkie elementy tablic D,
C i T to liczby naturalne. Można założyć, że rozwiązanie istnieje, t.j. da się przelecieć z A do B
zgodnie z warunkami zadania
"""

from egz1btesty import runtests
    
def planets( D, C, T, E ):
    E += 1
    n = len(D)
    cost = [[float("inf") for _ in range(E)] for _ in range(n)]
    cost[0][0] = 0
    
    for p in range(n-1):
        # Fueling (or not) on current planet:
        for e in range(1, E):
            cost[p][e] = min(cost[p][e], cost[p][e-1] + C[p])
        # We can fly by next planet, but don't buy fuel (same as landing and not fueling):
        for e in range(E - (D[p+1] - D[p])):
            cost[p+1][e] = min(cost[p+1][e], cost[p][e+D[p+1]-D[p]])
        
        # We can try teleporting:
        cost[T[p][0]][0] = min(cost[p][0] + T[p][1], cost[T[p][0]][0])
        
    return min(cost[n-1])

runtests( planets, all_tests = True )
