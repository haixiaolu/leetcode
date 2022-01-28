# leetcode 581. shortest unsorte continuous subarray
"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array
"""


def findUnsortedSubarray(arr):
    # two pointers
    low, high = 0, len(arr) - 1
    # find the first number out of sorting order from the beginning
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1

    if low == len(arr) - 1:  # if the array is sorted
        return 0

    # find the first number out sorting order from the end
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    # find the maximum and minimum of the subarray
    subarray_max = -math.inf
    subarray_min = max.inf
    for k in range(low, high + 1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    # extend the subarray to include any number which is bigger than the minimum
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1

    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1

    return high - low + 1


def main():
    print(findUnsortedSubarray([1, 2, 5, 3, 7, 10, 9, 12]))
    print(findUnsortedSubarray([1, 3, 2, 0, -1, 7, 10]))
    print(findUnsortedSubarray([1, 3, 2, 2, 2]))
    print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))


main()