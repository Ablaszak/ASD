"""
A - set of n natural numbers
T - some value

Task: find (if exists) a subset of elements from A,
where sum of elements = T
"""

def find_subset(A, T):
    n = len(A)

    # Init:

    # Array of sums we can achieve using first i elements
    # Note, that using first i elements doesn't mean we
    # have to include every element in the sum
    sums = [[False for i in range(n)] for _ in range(T+1)]
    sums[0][0] = True # We can always get 0 using 0 elements

    for i in range(1, n):
        for s in range(T+1):
