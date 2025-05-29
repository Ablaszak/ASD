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

    if(f.has_key((i, j, k))): # Co to jest???
        return f[(i, j, k)]

    f[(i, j, k)] = False

    if(i-A[k] >= 0):
        f[(i, j, k)] |= ferry(A, L, i-A[k], j, k-1, f)
    if(j-A[k] >=0):                         # |= oznacza "lub równa się"
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


















