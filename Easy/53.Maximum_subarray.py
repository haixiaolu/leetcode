"""
Question: Given an integer array nums, find the contiguoous subarrays (containing at least one number) 
          which has the largest sum and retun its sum

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)

        return global_max
