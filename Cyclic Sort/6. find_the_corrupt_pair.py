# leetcode 645.setMismatch
"""
Given an unsorted array containing 'n' numbers taken from the range 1 to n.
The array originally contained all the numbers from 1 to 'n', but due to the data error,
one of the numbers got duplicates which also resulted in one number going missing. 
Find both these numbers
"""
"""
Approach:
It shares Similarities with 'Find all Duplicate Numbers'
Following a similar approach:
    - place each number at its correct index
    - Once we done, iterate through the array to find the number in wrong index
    - Since only one number got corrupted:
        - The number at the wrong index is the duplicate
        - and the index itself represents the missing number
"""


def findErrorNums(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
    return [-1, -1]