# Task: find a path from a to b, that goes only on
# edges with descending weights

# Idea: we can use Djikstra with some modification in relaxation() function
# Sort all edges by length, do relaxation, go for it