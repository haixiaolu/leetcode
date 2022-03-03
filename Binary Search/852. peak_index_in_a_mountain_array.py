"""
Same approach with 162. 
However, 162 compare with right, to check if its greater than right
this problem is to check if its less than right
"""


def peakIndexMountain(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


print(peakIndexMountain([0, 2, 1, 0]))
