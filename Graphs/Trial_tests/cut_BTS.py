class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def is_leaf(node):
    if(node is None):
        return False # Works for this program

    if(node.left is None and node.right is None):
        return True
    return False

def cut_branch(node):
    if(node is None):
        return 0
    if(is_leaf(node.left) or is_leaf(node.right)):
        return node.value
    return min(cut_branch(node.left) + cut_branch(node.right), node.value)

def cutthetree(t):
    return (cut_branch(t.right) + cut_branch(t.left))

n1 = BNode(10)
n2 = BNode(3)
n3 = BNode(15)
n4 = BNode(11)
n5 = BNode(17)
n6 = BNode(-1)
n7 = BNode(-5)
n8 = BNode(0)

n1.left = n2         # 10 -> 3
n1.right = n3        # 10 -> 15
n2.parent = n1       # 3 -> 10
n3.parent = n1       # 15 -> 10

n3.left = n4         # 15 -> 11
n3.right = n5        # 15 -> 17
n4.parent = n3       # 11 -> 15
n5.parent = n3       # 17 -> 15

n2.left = n6         # 3 -> -1
n6.parent = n2       # -1 -> 3

n6.left = n7         # -1 -> -5
n6.right = n8        # -1 -> 0
n7.parent = n6       # -5 -> -1
n8.parent = n6       # 0 -> -1

print(cutthetree(n1))