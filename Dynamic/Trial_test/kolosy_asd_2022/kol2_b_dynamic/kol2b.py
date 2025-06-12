from kol2btesty import runtests
from queue import PriorityQueue

def min_cost( O, C, T, L ):
    n = len(O)
    park = [[O[i], C[i]] for i in range(n)]
    park.append([L, 0])
    park.append([0,0])
    park.sort()
    print(park)
    n = len(park)

    # [no cheat, cheat]
    d = [[float("inf"), float("inf")] for _ in range(n)]
    d[0][0] = 0

    for start in range(n-1):
        for stop in range(start+1, n):
            if(park[stop][0] - park[start][0] <= T):
                d[stop][0] = min(d[stop][0], d[start][0]+park[stop][1])
                d[stop][1] = min(d[stop][1], d[start][1]+park[stop][1])
            elif(park[stop][0] - park[start][0] <= 2*T):
                d[stop][1] = min(d[stop][1], d[start][0]+park[stop][1])
            else:
                break
    return min(d[n-1][0], d[n-1][1])




Ot = [17, 20, 11, 5, 12]
Ct = [9, 7, 7, 7, 3]
Tt = 7
Lt = 25

print(min_cost(Ot, Ct, Tt, Lt))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
