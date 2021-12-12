"""
Question: Given an array of intergs nums and an integer target, return indices of the two numbers
such that they add up to target
"""

"""
Answer: Use hashtable, it can decrease the searching time of target - x from O(n) to O(1)

we can create a hashtable
- for every x, we can search if there is target - x in the hashtable
- then insert x to hashtable, it can guarantee that x can not pair with itself
"""
from typing import List

# Hash table
def twoSum(nums: List[int], target: int) -> List[int]:
    # create a hashtable
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


## Time: O(n), we traverse the list containing n elements only once, each lookup in the table costs only O(1) time
## Space: O(n), the extra space required depends on the number of items stored in the hashtable, exactly n elements

# Brute Force
# def twoSum(nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i, j]


## Time: O(N^2)
## Space: O(1)


obj = twoSum(nums=[2, 7, 11, 15], target=9)
print(obj)