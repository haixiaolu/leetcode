# leetcode 268.Missing number
"""
Given an array containing n distinct numbers taken from the range 0 to n. Since the array has only
n number out of the total n + 1 numbers, find the missing number
"""
"""
Approach:
- follows Cyclic Sort approach
- Two differnece with Cyclic Sort:
-- number range 0 - n 
-- one extra number, we will not move to the next number after the swap until we have a correct number at index i
"""


def missingNumber(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]  # because the range is 0 - n, not 1 - n, so no need to - 1
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    # find the first number missing from its index, that will be the required number
    for i in range(n):
        if nums[i] != i:
            return i
    return n


def main():
    print(missingNumber([0, 1, 2, 4]))


main()