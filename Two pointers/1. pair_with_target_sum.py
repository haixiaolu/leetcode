# similar to leetcode 1.TwoSum
"""
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target
"""


def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]


def main():
    print(pair_with_target_sum([1, 3, 4, 5, 6], 7))
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))


main()