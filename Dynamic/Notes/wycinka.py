"""
Mamy las w postaci listy drzew, gdzie każde drzewo na wartość A[i]

Chcemy wyciąć drzewa generując największy zysk, ale z każdych 3 kolejnych drzew można wyciąć tylko 1
"""

"""
Pomysł:
Funckja: Maksymalny zysk ze ścięcia pierwszych i-1 drzew ścinając drzewo i

W funkcji sprawdzamy do 5 drzew w tył

f(i) = A[i] + max(f( i-5 ... i-1 )

"""

def forest(A):
    # warunki końca:


    n = len(A)
    F = [0 for _ in range(n)]
    F[0] = A[0] # for some reason