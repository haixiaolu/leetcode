# leetcode 448.Find all Numbers Disappeared in an Array
"""
Given an unsorted array containing numbers taken from the range 1 to 'n'. 
The array can have duplicates, which means some number will be missing. Find all those missing numbers
"""
"""
Approach:
It shares similarities with Find the Missing number. 
- follow a similar approach through "Find the Missing number" to place the number on their correct index
- once we are done with the cycle sort, iterate the array to find all indices that are missing the correct number
"""


def findDisappearedNumbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    missingNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)
    return missingNumbers


def main():
    print(findDisappearedNumbers([2, 4, 1, 2]))


main()
