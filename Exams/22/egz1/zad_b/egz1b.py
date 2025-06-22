from egz1btesty import runtests

class Node:
    def __init__( self ):
        self.left = None
        self.right = None
        self.level = None
        self.furthest = None

width = []
# O(n)
def add_levels(T, lvl=0): # go through the tree and write down level of every node
    T.level = lvl

    # Update width[]:
    global width
    if(len(width) <= lvl):
        width.append(1)
    else:
        width[lvl] += 1

    T.level = lvl
    T.furthest = lvl

    if(T.right is not None):
        T.furthest = max(T.furthest, add_levels(T.right, lvl+1))
    if(T.left is not None):
        T.furthest = max(T.furthest, add_levels(T.left, lvl+1))

    return T.furthest

# O(n)
def count_cuts(T, cutoff):

    # Recursion ends:
    if(cutoff == T.level): # now we cut off rest of the tree below
        ctr = 0
        if(T.left is not None):
            ctr += 1
        if(T.right is not None):
            ctr += 1
        return ctr

    if(T.furthest < cutoff):
        return 1 # we cut off this node

    ctr = 0
    if(T.left is not None):
        ctr += count_cuts(T.left, cutoff)
    if(T.right is not None):
        ctr += count_cuts(T.right, cutoff)
    return ctr


def widentall( T ):

    global width
    width = []
    add_levels(T)

    # get the level we want to cut off:
    w = 0
    lvl = 0
    for i in range(len(width)): # O(log(n))
        if(width[i] >= w):
            w = width[i]
            lvl = i


    # Now I have to check which branches lead to expected width
    # and cut those that don't

    return count_cuts(T, lvl)
"""
A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G
"""
#print(widentall(A))
runtests( widentall, all_tests = False )