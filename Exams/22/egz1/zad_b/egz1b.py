from egz1btesty import runtests

class Node:
  def __init__( self ):
        self.left = None
    self.right = None
    self.level = None

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

    if(T.right is not None):
        add_levels(T.right, lvl+1)
    if(T.left is not None):
        add_levels(T.left, lvl+1)

def widentall( T ):
    add_levels(T)
    global width
    w = max(width) # O(n)

    # Now I have to check which branches lead to expected width
    # and cut those that don't

    
    return None

runtests( widentall, all_tests = False )