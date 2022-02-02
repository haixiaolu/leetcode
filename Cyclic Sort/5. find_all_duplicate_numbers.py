# leetcode 442.Find all duplicates in an array
"""
Given an unsorted array containing 'n' numbers taken from the range 1 to 'n'.
The array has some number appearing twice, Find all these duplicate number without 
using any extra space
"""
"""
Approach:
It shares similarites with 'Find the Duplicate Number'
- follow the same approach, we will place each number in its correct indices. 
- After that, we will iterate through the array to find all numbers that are not at the correct indices.(they are duplicates)
"""


def findDuplicates(nums):
    i = 0
    for i in range(len(nums)):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    duplicateNumber = []
    for i in range(len(nums)):
        # all numbers that are not at the correct indices
        if nums[i] != i + 1:
            duplicateNumber.append(i + 1)
    return duplicateNumber
