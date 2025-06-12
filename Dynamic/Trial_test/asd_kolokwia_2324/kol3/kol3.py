from kol3testy import runtests

def orchard(A, m):
    n = len(A)
    T = sum(A)
    # Init:

    # Array of sums we can achieve using first i elements
    # Note, that using first i elements doesn't mean we
    # have to include every element in the sum.
    # Value of a place means how many trees are actually included
    sums = [-float("inf") for _ in range(T+1)]
    sums[0] = 0 # we can leave 0 trees and get 0 apples

    best = 0

    for i in range(n): # i for every tree
        for s in range(T, -1, -1):
            if(sums[s] >= 0):
                # if we cut the tree, the sums[s] stays the same
                # if we don't cut the tree:
                if(s+A[i] <= T):
                    sums[s+A[i]] = max(sums[s+A[i]], sums[s]+1)

    for t in range(m, T+1, m):
        best = max(best, sums[t])

    return (n-best)

Tt = [2, 2, 7, 5, 1, 14, 7]
m = 7
#print(orchard(Tt, m))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
