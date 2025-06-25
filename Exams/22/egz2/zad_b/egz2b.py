from egz2btesty import runtests

def gain(chest, d):
    if(chest == d[0]):
        return 0
    if(chest < d[0]):
        return chest-d[0]
    return min(chest-d[0], 10)

def magic( C ):

    # Init:
    n = len(C)
    max_gold = [-1 for _ in range(n)]
    max_gold[0] = 0

    # Main loop:
    for current in range(n-1):
        chest, d0, d1, d2 = C[current]
        d = [d0,d1,d2]
        take = min(chest, 10)

        # Try all doors:
        for i in range(3):
            if(d[i][1] != -1 and chest-10 <= d[i][0]): # door are openable
                if(d[i][0] <= chest+max_gold[current]): # we have enough gold to open door
                    max_gold[d[i][1]] = max(max_gold[d[i][1]], max_gold[current]+gain(chest, d[i]))

    return max_gold[n-1]


runtests( magic, all_tests = True )
