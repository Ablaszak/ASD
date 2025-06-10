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
    sums = [[False for i in range(T+1)] for _ in range(n+1)]
    sums[0][0] = True # We can always get 0 using 0 elements

    for i in range(1, n+1):
        for s in range(T+1):
            if(sums[i-1][s] == True):
                sums[i][s] = True # Because we can just not use the i'th element
                if(s + A[i-1] == T):
                    return True
                if(s + A[i-1] < T):
                    sums[i][s + A[i-1]] = True
    return False

print(find_subset([1,6,23,5,1234], 1235))