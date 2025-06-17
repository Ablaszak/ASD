"""
The robot moves through a two-dimensional maze and has to reach from position A = (xa, ya) to position
B = (xb, yb). The robot can perform the following movements:
1. move forward to the next square,
2. turn 90 degrees clockwise,
3. turn 90 degrees counterclockwise.

The rotation takes the robot 45 seconds. During the forward movement, the robot accelerates and it takes 60 seconds to cover
the first square, 40 seconds to cover the second, and 30 seconds to cover the next
square. Performing a rotation stops the robot and the following forward movements accelerate it
again. Please implement the function robot( L, A, B) which calculates the minimum number of seconds the robot needs to reach from point A to point B (or
returns None if this is impossible).
The function should be as fast as possible. Please estimate the time and memory complexity
of the algorithm used.
Maze. The maze is represented by an array of rows, each of which is a string
consisting of k columns. An empty character indicates a field in which the robot can move, and the character
'X' indicates a wall of the maze. The maze is always surrounded by walls and it is impossible to leave the board
"""

from queue import PriorityQueue

def accelerate(v):
    if(v == 30 or v == 45):
        return 30
    return 45

def dijkstra(G, s, end):
    # Initialization:
    rows = len(G)
    cols = len(G[0])

    t = [[float("inf") for _ in range(cols)] for _ in range(rows)]

    t[s[0]][s[1]] = 0 # <--- Very important, without this the algorithm won't start

    # visited[] contains lists of states achieved for every vertex
    # state template: [direction, velocity]
    visited = [[[] for _ in range(cols)] for _ in range(rows)]

    # queue element template:
    # (time of entrance, vertex coordinates, velocity (seconds per vertex), direction)
    pq = PriorityQueue()
    pq.put((t[s[0]][s[1]], s, 60, 1))

    # Main loop:
    while(not pq.empty()):
        time, [r, c], velocity, direction = pq.get()
        if([r, c] == end):
            return time

        if([direction, velocity] in visited[r][c]):
            continue # already achieved this state in better time

        visited[r][c].append([direction, velocity])

        # Relaxation for the newly found vertex:

        # Note: we don't have to check if we are going beyond the board,
        # because in content of the task it states that such case is not possible

        # go up:
        if(G[r-1][c] != 'X'):
            if(direction == 0):
                pq.put((time+accelerate(velocity), [r-1, c], accelerate(velocity), direction))
            else:
                pq.put((time+45+60, [r-1, c], 60, 0))

        # go right:
        if(G[r][c+1] != 'X'):
            if(direction == 1):
                pq.put((time+accelerate(velocity), [r, c+1], accelerate(velocity), direction))
            else:
                pq.put((time+45+60, [r, c+1], 60, 1))

        # go down:
        if(G[r+1][c] != 'X'):
            if(direction == 2):
                pq.put((time+accelerate(velocity), [r+1, c], accelerate(velocity), direction))
            else:
                pq.put((time+45+60, [r+1, c], 60, 2))

        # go left:
        if(G[r-1][c] != 'X'):
            if(direction == 3):
                pq.put((time+accelerate(velocity), [r, c-1], accelerate(velocity), direction))
            else:
                pq.put((time+45+60, [r, c-1], 60, 3))
    return None

"""
        for (v, length) in G[vertex]:
            if(t[v] > t[vertex] + length and visited[v] == False):
                t[v] = t[vertex] + length
                parent[v] = vertex
                pq.put((t[v], v))
"""

def robot(L, A, B):
    return dijkstra(L, A, B)

tests = [
    {
        'L':# 0123456789
            ["XXXXXXXXXX",  # 0
             "X X      X",  # 1
             "X XXXXXX X",  # 2
             "X        X",  # 3
             "XXXXXXXXXX",  # 4
             ],
        'A': (1, 1),
        'B': (8, 3),
        'sol': 440
    },
    {
        'L':# 0123456789
            ["XXXXXXXXXX",  # 0
             "X        X",  # 1
             "X XXXXXX X",  # 2
             "X XXXXXX X",  # 3
             "X        X",  # 4
             "XXXXXXXXXX",  # 5
             ],
        'A': (1, 1),
        'B': (8, 4),
        'sol': 425
    },
    {
        'L':  # 0123456789
            ["XXXXXXXXXX",  # 0
             "X        X",  # 1
             "X  XXXXXXX",  # 2
             "X        X",  # 3
             "X XXXXXX X",  # 4
             "X        X",  # 5
             "XXXXXXXXXX",  # 6
             ],
        'A': (1, 1),
        'B': (8, 4),
        'sol': 545
    },
    {
        'L':  # 01234567890123456789
            ["XXXXXXXXXXXXXXXXXXXX",  # 0
             "X      X           X",  # 1
             "X    X     X    X  X",  # 2
             "X X     X          X",  # 3
             "X   X       X     XX",  # 4
             "XX       X     X   X",  # 5
             "X    X       X     X",  # 6
             "X         X        X",  # 7
             "X     X       X    X",  # 8
             "XXXXXXXXXXXXXXXXXXXX",  # 9
             ],
        'A': (1, 1),
        'B': (18, 8),
        'sol': 1165
    },
    {
        'L':  # 01234567890123456789
            ["XXXXXXXXXXXXXXXXXXXX",  # 0
             "X      X           X",  # 1
             "X    X     X    X  X",  # 2
             "X X     X          X",  # 3
             "X   X       X     XX",  # 4
             "XX       X     X   X",  # 5
             "X    X       X     X",  # 6
             "X         X       XX",  # 7
             "X     X       X  X X",  # 8
             "XXXXXXXXXXXXXXXXXXXX",  # 9
             ],
        'A': (1, 1),
        'B': (18, 8),
        'sol': None
    },
    {  # 111111111122222222223333333333
        'L':  # 0123456789012345678901234567890123456789
            ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 0
             "X                                      X",  # 1
             "X                                      X",  # 2
             "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 3
             "X                                      X",  # 4
             "X                                      X",  # 5
             "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX",  # 6
             "X                                      X",  # 7
             "X                                      X",  # 8
             "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 9
             "X                                      X",  # 10
             "X                                      X",  # 11
             "X        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 12
             "X                                      X",  # 13
             "X                                      X",  # 14
             "X                                      X",  # 15
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X",  # 16
             "X                                      X",  # 17
             "X                                      X",  # 18
             "X                                      X",  # 19
             "X                                      X",  # 20
             "X                                      X",  # 21
             "X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 22
             "X                                      X",  # 23
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X",  # 24
             "X                                      X",  # 25
             "X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 26
             "X                                      X",  # 27
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 28
             ],
        'A': (1, 27),
        'B': (38, 1),
        'sol': 6580
    },
    {  # 111111111122222222223333333333
        'L':  # 0123456789012345678901234567890123456789
            ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 0
             "X  X     X     X                    X  X",  # 1
             "X X  X  X     X                     XXXX",  # 2
             "X   X  X  X  X  XXXXXXX     X     X    X",  # 3
             "X  X  X  X  X  X       X     X     X   X",  # 4
             "X X  X  X  X  X         X     X     X  X",  # 5
             "XX  X  X  X  X           X     X       X",  # 6
             "X  X  X  X  X             X     X      X",  # 7
             "X    X  X  X               X     X     X",  # 8
             "X   X  X  X                 X     X    X",  # 9
             "X  X  X  X                   X     X   X",  # 10
             "X X  X  X                     X     X  X",  # 11
             "XX  X  X       XXXXXXX         X       X",  # 12
             "X  X  X       X       X         X      X",  # 13
             "X X  X       X         X         X     X",  # 14
             "X   X       X           X         X    X",  # 15
             "X  X       X             X         X   X",  # 16
             "X X       X               X         X  X",  # 17
             "XX       X                 X         X X",  # 18
             "X       X                   X          X",  # 19
             "X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 20
             "X X     X     X     X     X     X    X X",  # 21
             "X          X               XXXX        X",  # 22
             "X         X X      XXXX    X   X       X",  # 23
             "X        X   X    X        X   X       X",  # 24
             "X       XXXXXXX    XXXX    X   X       X",  # 25
             "X      X       X       X   XXXX        X",  # 26
             "X                  XXXX                X",  # 27
             "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 28
             ],
        'A': (1, 1),
        'B': (38, 27),
        'sol': 14060
    }

]


def runtests(f):
    errors = 0
    for t in tests[:]:
        L = t['L']
        A = t['A']
        B = t['B']
        S = t['sol']

        for i in range(len(L)):
            print(L[i])
        print("A :", A)
        print("B :", B)
        print("oczekiwany wynik :", S)

        R = f(L, A, B)

        print("Uzyskany wynik   :", R)

        if R != S:
            print("Problem! Błędny wynik!")
            errors += 1
            continue

    print("===============================")
    if errors == 0:
        print('Wszystko OK!')
    else:
        print("Problemy!")
        print("Niezaliczone testy :", errors)

runtests(robot)