"""
Szalony Inwestor wybudował po południowej stronie drogi n biurowców, na pozycjach x0 < ⋯ <
xn−1. Parkingi tych biurowców mają dopiero zostać wybudowane i dostępne jest w tym celu m
działek (m ≥ n), dostępnych na północnej stronie drogi, na pozycjach y0 < ⋯ < ym−1. Inwestor
chce wybudować dokładnie po jednym parkingu dla każdego biurowca (żadne dwa biurowce nie
mogą dzielić tego samego parkingu). Zasady bezpiecznego ruchu wymagają, że i-ty biurowiec musi
mieć parking na pozycji wcześniejszej niż i + 1-szy. Inwestor chce wybudować parkingi na takich
pozycjach, żeby suma odległości parkingów od biurowców była minimalna. Odległość i-go biurowca
od j-ej działki to ∣xi − yj ∣. Zadanie polega na implementacji funkcji:
parking( X, Y )
która na wejściu otrzymuje listę X zawierającą n pozycji biurowców oraz listę Y zawierającą m
pozycji działek na parkingi (listy X oraz Y zawierają nieujemne liczby całkowite). Funkcja powinna
być możliwie jak najszybsza.
"""

from egz2btesty import runtests

states = [[]]

def get_sum(X, Y, b, p): # assign building b to parking p

    global states
    if(states[b][p] is not None):
        return states[b][p]

    if(b == 0):
        return abs(X[b] - Y[p])

    dist = abs(X[b] - Y[p])
    best = float("inf")
    newp = p
    while(newp > b): # have to be strong '>', not '>='
        newp -= 1 # assign parking p to building b-1
        best = min(best, dist + get_sum(X, Y, b-1, newp))
    states[b][p] = best
    return best


def parking(X,Y):
    n = len(X)
    m = len(Y)
    global states
    states = [[None for _ in range(m)] for _ in range(n)]
    # States says, what is the minimal sum of distances between
    # buildings and parking lots, if building i gets assigned to parking j
    p = m
    while(p > n-1):
        p -= 1
        states[n-1][p] = get_sum(X, Y, n-1, p)

    best = float("inf")
    for i in range(m):
        if(states[n-1][i] is not None):
            best = min(best, states[n-1][i])
    return best

runtests( parking, all_tests = True )
