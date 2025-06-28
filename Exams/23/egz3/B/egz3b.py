from egz3btesty import runtests

def merge_sort(T, left, right):
    # Recursion ends:
    if(right == left):
        return []

    if(right - left == 1):
        return [T[left]]

    mid = (right + left)//2

    array = merge_sort(T, mid, right)
    allay = merge_sort(T, left, mid)

    # merging:
    merged = [None for _ in range(right-left)]
    l, r, i = 0, 0, 0

    while(l < mid-left and r < right-mid):
        if(allay[l] <= array[r]):
            merged[i] = allay[l]
            l += 1
        else:
            merged[i] = array[r]
            r += 1
        i += 1

    # append unfinished array:
    while(l < mid-left):
        merged[i] = allay[l]
        l += 1
        i += 1
    while(r < right-mid):
        merged[i] = array[r]
        r += 1
        i += 1

    return merged

def is_cool(p1, p2):
    if(p1[0] < p2[0] < p1[1] <p2[1]): # we know they are sorted
        return False
    return True

def uncool( P ):
    n = len(P)
    # save id of every element:
    for i in range(n):
        P[i].append(i)
    P.sort()
    #merge_sort(P, 0, n)
    left = 0
    right = 1
    while(right < n):
        while(right < n and P[left][0] == P[right][0]):
            right += 1
        if(is_cool(P[left], P[right]) == False):
            return (P[left][2], P[right][2])
        right += 1
        while(P[left][1] < P[right][0] and P[left][0] < P[right][0]):
            left += 1

    return None


runtests( uncool, all_tests = True )
