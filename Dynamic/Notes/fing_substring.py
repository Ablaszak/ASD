"""
Cweloinatus rex
Złożoność: o(n^n!)
Uzasadnienie złożoności:
Bo widać
Uzasadnienie poprawności:
Wykorzystanie algorytmu bogo sort
UwU

"""

def find_substrings(a, b):
    # Init:
    lena = len(a)
    lenb = len(b)
    strings = [[0 for _ in range(lena+1)] for _ in range(lenb+1)]
    # (edges stays at 0)

    for ia in range(lena):
        for ib in range(lenb):
            if(a[ia] == b[ib]):
                strings[ib+1][ia+1] = strings[ib][ia] + 1
            else:
                strings[ib+1][ia+1] = max(strings[ib][ia+1], strings[ib+1][ia])

    w = 0
    for i in range(lenb + 1):
        w = max(w, max(strings[i]))
    return w

print(find_substrings("akrkkkdk", "ardgggk"))