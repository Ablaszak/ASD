"""
Żaba sobie siedzi (bardzo ważne)
Siedzi na polu nr 0
Mamy n pól
Żaba może wykonywać dowolne skoki, skok na odległość kosztuje ileś tam energii
C[i] = ile kcal kosztuje przeskoczenie o i pól do przodu
Na niektórych polach znjdują się przekąski
A[i] - ile kcal ma przekąska na polu i
Ma początku żaba ma 0 kcal

Pytanie:
    Ile minimalnie skoków musi wykonać żaba żeby dotrzeć do pola n-1

Można założyć, że C[i] <= i**2

Energia żaby nie może spaść poniżej 0
"""

"""
Pomysł:
Funkcja f(pole na którym jesteśmy, aktualna energia) = 
        = min liczba skoków potrzebna na dotarcie do tego pola
f(0, A[0]) = 0
f(0, cokolwiek inego) = inf 

f(i, e) = min( f(i-k, e-c[k]+przekąska) ) + 1; iterując k odpowiednio
Wynikiem jest 
minimum (iterując po energii bo musi być dowolna) ( f(n-1, e) )
Można ograniczyć energię do n**2, przy założeniu że po zjedzieniu
czegoś o energii >= n**2 skaczemy od razu na koniec
(wynika z warunków zadania)
"""














