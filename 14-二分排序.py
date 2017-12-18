import math

# 给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
# half = math.ceil((len(nums) / 2))
# if target < nums[half]:
#     return binarySearch(nums[0:half], target)
# elif target > nums[half]:
#     return binarySearch(nums[half:], target)
# else:
#     return half


def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if high == low:
            return high
        if nums[mid] >= target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
    return -1


print(binarySearch([1, 4, 4, 5, 7, 7, 8, 9, 9, 10], 1))
