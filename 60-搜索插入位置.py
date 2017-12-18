def searchInsert(A, target):
    if A == []:
        return 0
    for i, v in enumerate(A):
        if v == target:
            return i
        elif v > target:
            return i
    return len(A)


print(searchInsert([], 9))