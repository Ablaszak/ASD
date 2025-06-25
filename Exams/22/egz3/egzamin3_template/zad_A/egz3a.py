from egz3atesty import runtests
from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.mm = 0

q = deque()

def find_next_two(num):
    two = 2
    while(two <= num):
        two *= 2
    return two

# O(n)
def get_points(n, I):
    global q
    while(q): # cleanup for safety
        q.popleft()

    present = [False for _ in range(n)]
    for a, b in I:
        present[a] = True
        present[b] = True

    for i in range(n):
        if(present[i]):
            q.append(i)

# O(n log n)
def build_tree(n, it=0, tree_size=1):
    """
    Firstly we build left subtree
    Then give current node a value
    And AFTER this, we create right subtree
    """
    global q

    # recursion ends:

    # Ugly ending:
    if(len(q) == 0):
        return None

    # Pretty ending:
    if( tree_size >= n):
        return Node(q.popleft())

    # Normal work:

    # Prepare root:
    root = Node(None)

    #Build left side:
    root.left = build_tree(n, it+1, tree_size + 2**it)

    # Make root a valid node:
    root.val = q.popleft()

    # Build right side:
    root.right = build_tree(n, it, tree_size + 2**it)

    return root

# O(log n)
def let_it_snow(root, left, right):
    if(left <= root.val <= right):
        root.mm += 1

    if(left <= root.val and root.left is not None):
        let_it_snow(root.left, left, min(root.val, right))
    if(right >= root.val and root.right is not None):
        let_it_snow(root.right, max(root.val, left), right)

max_snow = 0
def find_max(root):

    if(root is None):
        return

    global max_snow
    max_snow = max(max_snow, root.mm)

    find_max(root.left)
    find_max(root.right)

def snow( T, I ):

    get_points(T, I)

    # We have to expand queue to be 2^x long
    global q
    points = len(q)
    n = find_next_two(points)
    for _ in range(n-points):
        q.append(T) # Fake value, nodes will never be used

    root = build_tree(n)
    for l, r in I:
        let_it_snow(root, l, r)

    global max_snow
    max_snow = 0
    find_max(root)

    return max_snow

runtests( snow, all_tests = False )