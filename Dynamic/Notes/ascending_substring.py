"""
O(n^2), but you get what you get, life is brutal
"""

def find_substring(string):
    # Init:
    n = len(string)
    # Array that says, what is the longest possible subset
    # that can be created with elements before and with i'th element
    longest = [1 for _ in range(n)]
    for end in range(n):
        for previous in range(end):
            if(string[previous] < string[end]):
                longest[end] = max(longest[previous], longest[end])
    return max(longest)