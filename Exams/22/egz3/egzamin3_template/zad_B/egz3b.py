from egz3btesty import runtests

def best_column(c, left, n):
    newtb = [-float("inf") for _ in range(n)]
    newbt = [-float("inf") for _ in range(n)]
    # Firstly, we are checking for entries
    # from left column and "entries" to current cell from above and below
    if(left[0] != -1 and c[0] != '#'):
        newtb[0] = max(newtb[0], left[0]+1)
    if(left[n-1] != -1 and c[n-1] != '#'):
        newbt[n-1] = max(newbt[n-1], left[n-1]+1)
    for i in range(1, n):
        if(c[i] != '#'):
            newtb[i] = max(newtb[i], newtb[i-1]+1, left[i]+1)
        if(c[n-i-1] != '#'):
            newbt[n-i-1] = max(newbt[n-i-1], newbt[n-i]+1, left[n-i-1]+1)
    """# Now we have to also check if there exists path from bottom to top
    for i in range(n-2, -1, -1):
        if(c[i] != '#'):
            new[i] = max(new[i], new[i+1]+1)
        if(c[])"""

    new = [max(newbt[i], newtb[i]) for i in range(n)]

    return new

def maze( L ):
    n = len(L)

    d = [[-float("inf") for _ in range(n)] for _ in range(n)]
    # init first column:
    d[0][0] = 0
    for i in range(1, n):
        if(L[i][0] == '#'):
            break
        d[i][0] = i

    # now go column by column:
    for c in range(1, n):
        left = [d[i][c-1] for i in range(n)]
        current = [L[i][c] for i in range(n)]
        best = best_column(current, left, n)

        for i in range(n):
            d[i][c] = best[i]
    #for i in range(n):
    #    print(d[i])
    if(d[n-1][n-1] == -float("inf")):
        return -1
    return d[n-1][n-1]



"""L = [
  "....",
  ".#..",
  ".#..",
  "...."
]"""

#print(maze(L))

runtests( maze, all_tests = True )
