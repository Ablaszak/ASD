"""
Przy nabrzeżu stoi prom o dwóch pokładach
Między pokładami jeżdżą samochody, ale muszą przejeżdżać wg kolejki

Samochody mają swój rozmiar (chyba)

Trzeba obliczyć ile maksymalnie samochodów zmieści się na obu pokładach
"""

"""
Pomysł:

Potrzebujemy wiedzieć, ile miejsca zostało na górnym i dolnym
pokład, oraz ile samochodów wjechało na statek

Funkcja: f(i, j, k) = czy jest możliwe, żeby na górnym pokładzie
zotało ZAJĘTE i miejsca, na dolnym j miejsca, 
oraz w sumie na statek wjechało k samochodów

Wyrażenie rekurencyjne:
(numerujemy samochody od 1, żeby 0 oznaczało brak samochodów)
f(i, j, k) = f(i-A[k], j, k-1) lub f(i, j-A[k], k-1)

f(i, j, 0) = True (zawsze możemy zmieścić 0 samochodów [chyba])

Wywołanie funkcji:
    max po wartościach k takich, że f(L, L, k) = True
"""

# Realna implementacja:

def ferry(A, L, i, j, k, f):

    if(k == 0):
        return True

    if((i, j, k) in f): # Już rozpatrywaliśmy?
        return f[(i, j, k)]

    f[(i, j, k)] = False

    if(i-A[k] >= 0): # Można zmieścić na górny pokład
        f[(i, j, k)] |= ferry(A, L, i-A[k], j, k-1, f)
    if(j-A[k] >=0): # Można zmieścić na dolny pokład
        f[(i, j, k)] |= ferry(A, L,i, j-A[k], k-1, f)

    return f[(i, j, k)]

def main(A, L):
    # Tworzenie słownika:
    f = dict()
    for i in range(L):
        for j in range(L):
            f[(i, j, 0)] = True

    # Poniższa pętla jest trochę zepsuta ale wystarczy posidzieć nad indeksami:
    wynik = len(A)
    for k in range(len(A)):
        if(ferry(A, L, 0, 0, k, f) == False):
            wynik = k-1
            break

    return wynik


# Moja implementacja:

# top & bot indicates how much space is occupied on top and bottom levels
def fit(C, size, top, bot, i, dic):

    print("robię ", i, "-ty samochód")
    if(top == bot == size): # We won't fit anymore
        return

    if((i, top, bot) in dic): # check if we haven't already calculated this case
        return

    dic[(i, top, bot)] = True

    if(i < len(C)): # There are still some cars left
        if(top + C[i] <= size):
            fit(C, size, top+C[i], bot, i+1, dic)
        if(bot + C[i] <= size):
            fit(C, size, top, bot + C[i], i + 1, dic)

cars=[1, 5, 2, 54, 1, 23]
L = 6
# Main loop:
f = dict() # dict says if we can achieve combination: (cars used, top space occupied, bottoms space occupied)
f[(0, 0, 0)] = True
fit(cars, L, cars[0], 0, 1, f) # first car goes on top
fit(cars, L, 0, cars[0], 1, f) # first car goes on bottom

print(max(f))















