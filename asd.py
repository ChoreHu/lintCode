import math

# @param nums: The integer array
# @param target: Target number to find
# @return the first position of target in nums, position start from 0


def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if high == low:
            return high
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] <= target:
            low = mid + 1
    return -1


print(binarySearch([2, 6, 8, 13, 15, 17, 17, 18, 19, 20], 15))
