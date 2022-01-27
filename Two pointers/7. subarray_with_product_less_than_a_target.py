# leetcode 713. subarray product less than k
"""
Given an array with positive numbers and a positive target number. find all of its contiguous subarray whose 
product is less than the target number
"""


def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
