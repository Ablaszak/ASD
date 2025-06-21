from zad3testy import runtests

class Node:
    def __init__( self ):
        self.left = None # lewe poddrzewo
        self.right = None # prawe poddrzewo
        self.parent = None # rodzic drzewa jeśli istnieje
        self.key = None # klucz

# The path look like this:
#   0 = turn left
#   1 = turn right
def find_path(num):
    path = []
    while(num > 1):
        path = [num%2] + path
        num //= 2
    return path

def get_value(root, num):
    path = find_path(num)
    n = len(path)
    curr = root
    for i in range(n):
        if(path[i] == 0): # turn left
            curr = curr.left
        else:             # turn right
            curr = curr.right

    return curr.key

def maxim(T, C):
    m = len(C)
    w = -float("inf")

    for i in range(m):
        w = max(w, get_value(T, C[i]))

    return w



runtests(maxim)