"""
Given an array containing n objects. Write a function to sort the objects in-place on their creation sequence number 
in O(n) and without using any extra space
"""
"""
Approach:
iterate the array one number at a time, and if the current number we are iterating is not
at the correct index, we swap it with the number at its correct index
"""


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        # print(j)
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([2, 3, 5, 4, 1]))


main()