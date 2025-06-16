"""
simple quick sort algorithm using Lomuto partition
"""

def qsort(T, left, right):

    if(right <= left): # end of recursion
        return

    # init:
    n = right
    pivot = T[n-1]

    # partition:
    i = left - 1
    for j in range(left, n-1):
        if(T[j] < pivot):
            i += 1
            T[j], T[i] = T[i], T[j]

    # Lastly - put pivot on the right spot:
    i += 1
    n -= 1
    T[i], T[n] = T[n], T[i]

    # sort both sides:
    qsort(T, left, i)
    qsort(T, i+1, right)


arr = [1,6,2,1, 23,4534256 ,6,7,345,6,4536,25426]
qsort(arr, 0, len(arr))
print(arr)