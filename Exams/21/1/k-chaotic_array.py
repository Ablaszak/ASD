"""
We say that an array T has a disorder factor of k (is k-Chaotic)
if two conditions are met:

1. the array can be sorted non-decreasingly by moving each element of A[i] by at most k positions
(after sorting it is in a position different from i by at most k)

2. the array cannot be sorted non-decreasingly by moving each element by less than k positions
"""
def merge_sort(T, left, right):
    # Recursion ends:
    if(right == left):
        return []

    if(right - left == 1):
        return [T[left]]

    mid = (right + left)//2

    array = merge_sort(T, mid, right)
    allay = merge_sort(T, left, mid)

    # merging:
    merged = [None for _ in range(right-left)]
    l, r, i = 0, 0, 0

    while(l < mid-left and r < right-mid):
        if(allay[l] <= array[r]):
            merged[i] = allay[l]
            l += 1
        else:
            merged[i] = array[r]
            r += 1
        i += 1

    # append unfinished array:
    while(l < mid-left):
        merged[i] = allay[l]
        l += 1
        i += 1
    while(r < right-mid):
        merged[i] = array[r]
        r += 1
        i += 1

    return merged

def chaos_index( T ):
    ids = [[T[i], i] for i in range(len(T))]
    ids = merge_sort(ids, 0, len(ids))
    w = 0
    for i in range(len(ids)):
        w = max(w, abs(ids[i][1] - i))
    return w

#print(chaos_index([1,2,3,4,3]))

x1 = [0, 2, 1.1, 2]
k1 = 1

x2 = [42]
k2 = 0

x3 = [2, 1]
k3 = 1

x4 = [5, 1, 2, 3, 4]
k4 = 4

x5 = [5, 4, 3, 2, 1]
k5 = 4

x6 = [10e22, 1, 10e-16, 100]
k6 = 3

x7 = [1, 1, 1, 1, 1]
k7 = 0

x8 = [1, 2, 1, 2, 1, 2]
k8 = 2

TESTS = [
    (x1, k1),
    (x2, k2),
    (x3, k3),
    (x4, k4),
    (x5, k5),
    (x6, k6),
    (x7, k7),
    (x8, k8)
]


def runtests(f):
    OK = True
    print("hi")
    for x, k in TESTS:
        print("--------")
        print("x = ", x)

        RESULT = f(x)
        print("oczekiwana odpowiedź: k =", k)
        print("uzyskana   odpowiedź: k =", RESULT)
        if RESULT != k:
            OK = False
            print("Problem!")

    if OK:
        print("OK!")
    else:
        print("Problemy!")

runtests( chaos_index )