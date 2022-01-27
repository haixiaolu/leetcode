# similar to leetcode 977.Squares of a Sorted Array
"""
Given a sorted array, create a new array containing squares of all the numbers of the input array
in the sorted order
"""


def sorted_squares(nums):
    n = len(nums)
    squares = [0 for x in range(n)]  # same as [0] * len(nums)
    highest_square_idx = n - 1
    left, right = 0, n - 1
    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        # whichever pointer gives us the bigger square
        if left_square > right_square:
            # we add it to the result array
            squares[highest_square_idx] = left_square
            # and move to the next/previous number
            left += 1
        else:
            squares[highest_square_idx] = right_square
            right -= 1
        highest_square_idx -= 1
    return squares


def main():

    print("Squares: " + str(sorted_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(sorted_squares([-3, -1, 0, 1, 2])))


main()