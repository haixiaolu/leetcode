"""
经典模版一
"""


def search(nums, target):

    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            nums = mid - 1
    return -1