from zad1testy import runtests

def bucket(I, x, y):
    span = y-x
    n = len(I)
    by_start = [[] for _ in range(y)]
    by_end = [[] for _ in range(y)]
    for el in I:

        if(el[0] < x or el[1] > y): # unusable element
            continue

        by_start[el[0]].append(el)
        by_end[el[1]].append(el)

    return by_start, by_end

def intuse(I, x, y):
    n = len(I)
    starts, ends = bucket(I, x, y)

    usable = [False for _ in range(n)]

    def traceback(el):
        if(el[0] == x):

    for last in ends:
        if(last[1] != y):
            break



answer = []
def create_set(I, used, it, n, num, y):
    ret = False
    for i in range(it, n):
        if(I[i][0] == num): # found next element

def intuse_n2(I, x, y):
    global answer
    n = len(I)
    answer = [False for _ in range(n)]

    return []

runtests(intuse)