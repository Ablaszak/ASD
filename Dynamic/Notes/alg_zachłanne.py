"""
SZEREGOWANIE ZADAŃ

Dane:

Ciąg przedziałów opisujących czas trwania pewnych zajęć
Przedziały są podane jako ?

Zadanie:
Należy wybrać jak najwięcej zajeć które na siebie nie nachodzą

Pomysły:

1. Wybieramy najkrótsze przedziały (błędne)

2. Wybranie przedziału który zaczyna się jak najwcześniej (błędne)

3. Wybieramy przedział który przecina jak najmniej konfliktów (błędne)

4. Poprawna strategia:
    Wybieramy przedział który KOŃCZY się najwcześniej

Dowód poprawności:
    1. Pierwszy krok algorytmu nigdy nie popełni błędu
    2. Wykazanie optymalnej podstruktury
        (po wykonaniu pierwszego korku, cały problem zamienia
        się w mniejszy wariant początkowego problemu)

---------------------------------------

KODY HUFFMANA

Obserwacja:
Kody binarne gdzie każdy symbol jest kodowany na tej samej liczbie
bitów nie zawsze są optymalne

Kod prefiksowy: kod, którego zapis każdego symbolu NIE jest
prefiksem żadnego innego kodu/zapisu symbolu.
Można to reprezentować jakoś takie śmieszne drzewo (opis poniżej)

Notacja:
    s - symbol
    f(s) - liczba wystąpień s
    T - drzewo kodujące
    d(s) - długość kodu symbolu s

Formułowanie algorytmu zachłannego budującego drzewo kodujące:

Powtarzaj aż powstanie drzewo (zostanie 1 węzeł):
    1. Weź 2 symbole o najmniejszej f(s) (x i y)
    2. Połącz je w nowy symbiol z taki, że f(z) = f(x) + f(y)
        realnie to wygląda tak że z jest korzeniem a x i y liśćmi małego drzewa


"""

























