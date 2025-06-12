from kol3testy import runtests

def orchard(A, m):
    n = len(A)
    T = sum(A)
    # Init:

    # Array of sums we can achieve using first i elements
    # Note, that using first i elements doesn't mean we
    # have to include every element in the sum.
    # Value of a place means how many trees are actually included
    sums = [[-float("inf") for i in range(T+1)] for _ in range(n+1)]
    sums[0][0] = 0 # we can leave 0 trees and get 0 apples

    best = 0
    candidates = []

    for i in range(1, n+1):
        for s in range(T+1):
            if(sums[i-1][s] >= 0):
                sums[i][s] =  max(sums[i][s], sums[i-1][s]) # Because we can just not use the i'th element
                # Here is A[i-1] because indexes don't exist xD
                if(s + A[i-1] <= T):
                    sums[i][s + A[i-1]] = max(sums[i][s+A[i-1]], sums[i-1][s]+1) # (trees included before, trees included in [i-1][s] + the new tree)
    for t in range(m, T+1, m):
        best = max(best, sums[n][t])

    return (n-best)

#Tt = [2, 2, 7, 5, 1, 14, 7]
#m = 7
#print(orchard(Tt, m))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=False)
