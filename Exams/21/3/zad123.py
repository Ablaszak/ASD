"""
Third task:
"""

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0

def run_node(word, root):
    return

def count_super(root):
    return

def double_prefix(L):
    n = len(L)

    # Build a tree by running every node:
    root = Node()
    for i in range(L):
        run_node(L[i], root)

    # Check every node if it is a super nice word:
    ctr = 0
    if(root.left is not None):
        ctr += count_super(root.left)