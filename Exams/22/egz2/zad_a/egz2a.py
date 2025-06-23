from egz2atesty import runtests

class Node:
    def __init__(self):
        self.max_left = None
        self.max_right = None
        self.max_cap = None
        self.left = None
        self.right = None
        self.iswarehouse = False

class Warehouse:
    def __init__(self, num, cap):
        self.num = num
        self.cap = cap
        self.iswarehouse = True

def find_next_two(num):
    two = 2
    while(two < num):
        two *= 2
    return two

wnum = 0
last = None

def build_segment_tree(n, l, r, T, i=0): # n = number of leafs

    root = Node()
    root.max_left = T
    root.max_right = T

    # Recursion end:
    if (2**(i+1) >= n): # next level should be leaves
        global wnum
        root.left = Warehouse(wnum, T)
        root.right = Warehouse(wnum+1, T)
        wnum += 2
        return root

    root.left = build_segment_tree(n, l, r//2, T, i+1)
    root.left = build_segment_tree(n, (r//2) + 1, r, T, i+1)

    return root

def put_coal(T, c):

    # Recursion end:
    if(T.iswarehouse):
        global last
        last = T.num
        T.cap -= c

        return T.cap

    if(T.max_left >= c):
        T.max_left = put_coal(T.left, c)
    else:
        T.max_right = put_coal(T.right, c)

    # This return lets the parent know what is the highest
    # coal cap in this subtree
    return max(T.max_left, T.max_right)

def coal( A, T ):
    global wnum
    global last
    wnum = 0
    last = None
    n = find_next_two(len(A))

    return -1

runtests( coal, all_tests = False )
