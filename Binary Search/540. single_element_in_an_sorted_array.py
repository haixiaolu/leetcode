"""
1. Binary Search on Evens indexes only

 - dividing left and right in the usual way, but then decrementing it by 1 if it is odd
 - this also ensures that if we have an even number of even indexes to search, that we are getting the lower middle(incrementing by 1
   here would not work, will be infinite loop)
- Then we check if the mid index is the same as the one after it
    - if it is, it's not single element, and that the single element must be at an even index after mid
        - therefore, we set left to be mid + 2, because we want it to point at an even index
    - if it is not, then we know that the single element is either at mid or at some index before mid, so we set right to be mid 
    - once left == right, the search space is down to 1 element, and this must be the single element, return it 
"""


def singleNonDuplicates(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid
    return nums[left]
