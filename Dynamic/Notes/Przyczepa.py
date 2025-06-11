"""
Mamy przyczepę i pojemności T
Mamy towary, które należy załadować na przyczepę,
każdy towar ma objętość będącą potęgą dwójki

Chcemy przyczepę zapełnić jak najbardziej,
używając jak najmniej towarów

(Wypełnienie przyczepy bardziej, większą liczbą towarów, jest lepsze, niż wypełnienie mniej ale mniejszą liczbą towarów)
"""

"""
We have a trailer with capacity T.

We also have goods that need to be loaded onto the trailer, 
where each good has a volume that is a power of two.

Our goal is to fill the trailer as much as possible, 
using as few goods as possible.

(A higher fill level using more goods is better than a lower fill level using fewer goods.)
"""

def fit(i, space_left, used):

    if(space_left < 0):
        return (float("inf"), 0, 0)

    if(space_left == 0 or i == 0):
        return (space_left, len(used), used)

    dont_take = used
    take = used + [i]

    return min(
                fit(i-1, space_left, dont_take), # We don't take i'th element
                fit(i-1, space_left-vol[i], take) # We take
               )


vol = [2, 4, 2, 8, 32, 8, 1]
vol.sort()
T = 16
print(fit(len(vol)-1, T, []))
