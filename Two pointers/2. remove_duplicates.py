# leetcode 26. Remove duplicates from sorted array
"""
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates
in place, return the length of the subarray that has no duplicate in it 
"""


def remove_duplicates(arr):
    # index of the next non_duplicate element
    next_non_duplicate = 1  # the first position is always not a duplicate
    fast = 1
    while fast < len(arr):
        if arr[next_non_duplicate - 1] != arr[fast]:
            arr[next_non_duplicate] = arr[fast]
            next_non_duplicate += 1
        fast += 1
    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()