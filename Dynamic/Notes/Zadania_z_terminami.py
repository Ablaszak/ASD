"""
Mamy listę zadań Z
Wykonanie każdego zadania zajmuje godzinę czasu
Dla każdego zadania mamy deadline (po ilu godzinach zadanie musi być wykonane)
Za każde zadanie mamy nagrodę (g(zi))

Niektórych zadań można nie wykonać, ale chcemy zmaksymalizować zysk

"""

def greedy(Z, G, D):
    n = len(Z)
    qu = [-1 for _ in range(max(D))]
    chosen_ctr = 0
    tasks = sorted([[D[i], G[i]] for i in range(n)])
    for i in range(n):
        dead = tasks[i][0] - 1 # because we should start it an hour early and time=0 es equal to starting a task right now
        while(dead >= 0):
            if(qu[dead] == -1):
                qu[dead] = tasks[i][1]
                chosen_ctr += 1
                break

