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

Tt = [1234,21,213,5,1,234,1,2,3,1,23]
print(merge_sort(Tt, 0, len(Tt)))