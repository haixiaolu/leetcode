"""
Question: given a sorted array of distinct integers and a target value, return the index if the target is found. 
          if not, return the index where it would be if it were inserted in order.

          You must write an algorithm with O(log n) runtime complexity
"""

"""
思路： 二分查找
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
