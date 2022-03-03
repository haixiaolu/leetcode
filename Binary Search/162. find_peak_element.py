"""
1. If the element happens to be lying in a descending sequance of numbers, or a local slope(found by comparing nums[i]
   to its right), it means that the peak will always lie towards the left, so [left, mid] is the range
2. if the middle element, mid lies in an ascenidng sequence of number, or a rising slope(found by comparing nums[i] to right), 
   it implies that the peak will always lie towards the right, so [mid, right] is the range
3. In this way, we keep on reducing the search space till we eventually reach a state when only one element is remaining
   in the search space. This single element is the peek element.
"""


def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


print(findPeakElement([1, 2, 3, 1]))