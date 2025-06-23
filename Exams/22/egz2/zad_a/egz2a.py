from egz2atesty import runtests

class Node:
    def __init__(self):
        self.range_left = None
        self.range_right = None
        self.max_cap = None
        self.left = None
        self.right = None

class Warehouse:
    def __init__(self, num, cap):
        self.num = num
        self.cap = cap

def find_next_two(num):
    two = 2
    while(two < num):
        two *= 2
    return two

wnum = 0

def build_segment_tree(n, l, r, T, i=0): # n = number of leafs


    root = Node()
    root.range_left = l
    root.range_right = r
    root.max_cap = T

    # Recursion end:
    if (i * i >= n):
        global wnum
        root.left = Warehouse(wnum, T)
        root.right = Warehouse(wnum+1, T)
        T += 2
        return root

    root.left = build_segment_tree(n, l, r//2, T, i+1)
    root.left = build_segment_tree(n, (r//2) + 1, r, T, i+1)

    return root

def coal( A, T ):
    global wnum
    wnum = 0
    n = len(A)
    return -1

runtests( coal, all_tests = False )
