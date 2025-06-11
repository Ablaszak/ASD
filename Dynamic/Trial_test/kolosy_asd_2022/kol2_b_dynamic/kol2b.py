from kol2btesty import runtests
from queue import PriorityQueue

def min_cost( O, C, T, L ):
    n = len(O)
    park = [[O[i], C[i]] for i in range(n)]
    park.sort()
    park = [0,0] + park
    n = len(park)
    pq = PriorityQueue()
    pq_cheat = PriorityQueue()

    # Window indexes:
    right = 0
    left = 0

    # Main loop:
    while(right < park[n-1][0]):
        while(abs(O[right][0] - O[left][0]) < T)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = False )
