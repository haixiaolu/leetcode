# leetcode 75. sort colors
"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as
objects, we can't count 0s, 1s and 2s to recreate the array
"""


def sortColors(nums):
    # all element < low are 0 and > high are 2
    # all element >= low < i are 1
    low, high = 0, len(nums) - 1
    i = 0
    while i <= high:
        if nums[i] == 0:
            nums[i], nums[low] = nums[low], nums[i]
            # increrment 'i' and 'low'
            i += 1
            low += 1
        elif nums[i] == 1:
            low += 1

        else:
            nums[i], nums[high] = nums[high], nums[i]
            # decrement 'high' only, after the swap the number at index 'i'
            # could be 0s, 1s and 2s


def main():
    arr = [1, 0, 2, 1, 0]
    sortColors(arr)
    print(arr)


main()