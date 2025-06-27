from egz2btesty import runtests

def gain(chest, d):
    if(chest < d[0]):
        return chest-d[0]
    return min(chest-d[0], 10)

def openable(door, pocket, chest):
    if(door[1] == -1): # Door leads to nowhere
        return False
    if(door[0] < chest-10): # There is too much gold in the chest
        return False
    if(chest + pocket < door[0]): # We don't have enough gold
        return False
    return True

def magic( C ):

    # Init:
    n = len(C)
    max_gold = [-1 for _ in range(n)]
    max_gold[0] = 0

    # Main loop:
    for current in range(n-1):
        chest, d0, d1, d2 = C[current]
        d = [d0,d1,d2]

        # Try all doors:
        for i in range(3):
            if(openable(d[i], max_gold[current], chest)):
                max_gold[d[i][1]] = max(max_gold[d[i][1]], max_gold[current]+gain(chest, d[i]))

    return max_gold[n-1]


runtests( magic, all_tests = True )
