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
    pq = PriorityQueue()
    pq_cheat = PriorityQueue()

    # Queue scheme: (summary cost, parking number, did we cheat on the way)
    pq.put((0, 0, False))
    #pq_cheat.put((0, 0, False))
    # Window indexes:
    right = 0
    right2 = 0
    # Main loop:
    for left in range(n):
        # Get rid of old stations:
        while(pq.queue[0][1] < left):
            pq.get()
        #while(pq_cheat.queue[0][1] < left):
        #    pq_cheat.get()

        if(left == n-1): # We got to our destination
            return pq.get()

        # Widen window:
        while(right<n and abs(park[right][0] - park[left][0]) <= T):
            pq.put((pq.queue[0][0] + park[right][1], right, pq.queue[0][2]))
            pq_cheat.put((pq.queue[0][0] + park[right][1], right, pq.queue[0][2]))
            right += 1
        # Widen cheat window:
        if(pq.queue[0][2] == False):
            right2 = right
            while(right2 < n and abs(park[right2][0] - park[left][0]) <= 2*T):
                pq.put((pq.queue[0][0] + park[right2][1], right2, True))
                right2 += 1


Ot = [17, 20, 11, 5, 12]
Ct = [9, 7, 7, 7, 3]
Tt = 7
Lt = 25

print(min_cost(Ot, Ct, Tt, Lt))
# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( min_cost, all_tests = False )
