from kol2btesty import runtests
from collections import deque

def min_cost(O, C, T, L):
    n = len(O)
    parks = [[O[i], C[i]] for i in range(n)]
    parks.append([0,0])
    parks.append([L, 0])
    parks.sort()
    n = len(parks)

    parent = [None for _ in range(n)]
    cost = [float("inf") for _ in range(n)]
    cost[0] = 0

    # [cost, parking number]
    dq = deque()
    dq.append([0, 0])

    for right in range(1, n):
        # clean up old elements:
        while(len(dq) > 0 and parks[right][0]-parks[ dq[0][1] ][0] > T):
            dq.popleft()
        # update cost array (we can do it, because we know that most left
        # element in the deque is cheapest to get to from all elements
        # that we can use as a starting point getting to the 'right' element
        cost[right] = dq[0][0] + parks[right][1]
        parent[right] = dq[0][1]

        # Now, check if the new (right) element is cheaper to get to
        # than other elements before it:
        while(len(dq) > 0 and dq[-1][0] >= cost[right]):
            dq.pop()
        dq.append([cost[right], right])

    # We have to think, which parking we want to skip:
    max_price = 0
    parking = n-1
    while(parking != 0):
        max_price = max(max_price, parks[parking][1])
        parking = parent[parking]
    return (cost[n-1] - max_price)

Ot = [17, 20, 11, 5, 12]
Ct = [9, 7, 7, 7, 3]
Tt = 7
Lt = 25

print(min_cost(Ot, Ct, Tt, Lt))
# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( min_cost, all_tests = False )

