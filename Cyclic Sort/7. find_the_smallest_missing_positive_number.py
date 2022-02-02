# leetcode 41. First missing positive
"""
Given an unsorted array containing numbers, find the smallest missing positive number in it
"""
"""
Approach:
It shares similarities with 'Find the Missing Number' with one big difference
    - In this problem, the numbers are not bound by any range so we can have any number in the input array
follow similar approach:
- place the numbers on their correct indices and ignore all numbers that are out of the range (negatives and > length.array)
- Onece we are done, iterate the array and the first index that does not have the correct number will be the 
  smallest missing positive number
"""


def findMissingPositve(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1  # 因为有负数， 所以位置要加一
