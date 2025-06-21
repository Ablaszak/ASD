from zad2testy import runtests
"""
2nd task:
"""

class Node:
    def __init__(self):
        self.children = [None, None]
        self.val = 0

def print_tree(root, prefix=""):
    if root is None:
        return
    print(f"{prefix} (val={root.val})")
    if root.children[0] is not None:
        print_tree(root.children[0], prefix + "0")
    if root.children[1] is not None:
        print_tree(root.children[1], prefix + "1")

def run_node(word, root, level=0): # root = level 0

    root.val += 1
    if(level == len(word)):
        return


    if(root.children[int(word[level])] is None):
        root.children[int(word[level])] = Node()

    run_node(word, root.children[int(word[level])], level+1)

def find_super(root, word=""):

    if(root is None or root.val <= 1): # end recursion
        return []

    # check if root is not super:
    super_nice = True
    if (root.children[0] is not None):
        if(root.children[0].val >= 2):
            super_nice = False
    if (root.children[1] is not None):
        if(root.children[1].val >= 2):
            super_nice = False

    if(super_nice == True and root.val >= 2):
        return [word]

    # Now, keep looking for super nice words:

    w = []

    if(root.children[0] is not None):
        w += find_super(root.children[0], word+'0')
    if(root.children[1] is not None):
        w += find_super(root.children[1], word+'1')

    return w

def double_prefix(L):
    n = len(L)

    # Convert strings to
    # Build a tree by running every node:
    root = Node()
    for i in range(n):
        run_node(L[i], root)
    #print_tree(root)
    # Check every node if it is a super nice word:
    return find_super(root)

#print(double_prefix(['010', '011', '101', '1']))
runtests( double_prefix )
