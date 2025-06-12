from zad8testy import runtests

def f(X, Y, i, j):
    if(i>j or i<0 or j<0):
        return None

    current = float("inf")
    w = float("inf")

    if(i==0): # we will be ending here
        for p in range(j):
            w = min(w, abs(X[0]-Y[p]))
        return w

    if(i==j): # Also ending here
        w=0
        for p in range(j):
            w += abs(X[p]-Y[p])
        return w

    while (current is not None):
        w = min(w, abs(X[i]-Y[j])+current)

        j -= 1 # indicates last parking space

        current = f(X, Y, i-1, j)

    return w

def parking1(X,Y):
    if(len(X) == len(Y)):
        w=0
        for i in range(len(X)):
            w += abs(X[i]-Y[i])
        return w

    current=float("inf")
    n = len(Y)
    m = len(X)
    w = float("inf")

    for p in range(m, n):
        w = min(w, abs(X[m-1]-Y[p]) + parking(X[:m-1], Y[:p-1]))

    return w

pass
def parking(X, Y):
    n, m = len(X), len(Y)
    # dp[j] = koszt dopasowania X[0] → Y[j]
    dp = [abs(X[0] - Y[j]) for j in range(m)]

    for i in range(1, n):
        new_dp = [float('inf')] * m
        best = float('inf')
        for j in range(i, m):
            best = min(best, dp[j-1])
            new_dp[j] = best + abs(X[i] - Y[j])
        dp = new_dp

    return min(dp[n-1:])

#X = [3,6,10,14]
#Y = [1,4,5,10,11,13,17]
#print(parking(X, Y))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
