# We have weighted tree
# We want to find vertex with the shortest distance to the most remote leaf
"""
Idea 1:
We can find two most remote leafs and
    a) check all vertexes in path between them
    b) or we can find a middle vertex by median
How to find two leafs:
    Start on a random vertex and count distance to all leafs
    Find the furthest leaf, if there's more than one, choose a random leaf (there are max 2 leafs)
    Run distance() function again, starting from a newly found leaf, find the furthest leaf from new start
    We now hasve the longest path between two leafs

"""