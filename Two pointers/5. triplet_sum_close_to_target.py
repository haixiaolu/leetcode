# leetcode 16. 3sum closet
"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the 
target number as possible, return the sum of the triplet. if there are more than one such triplet,return the sum 
of the triplet with the smallers sum 
"""
import math


def three_sum_closest(nums, target_sum):
    nums.sort()
    smallest_difference = math.inf

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            target_diff = target_sum - nums[i] - nums[left] - nums[right]
            if target_diff == 0:  # we've found a triplets with an exact sum
                return target_sum

            # the second part of the following 'if' is to handle the smallest sum
            # when we have more than one solution
            if abs(target_diff) < abs(smallest_difference) or (
                abs(target_diff) == abs(smallest_difference)
                and target_diff > smallest_difference
            ):
                smallest_difference = (
                    target_diff  # save the closest and the biggest difference
                )

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

        return target_sum - smallest_difference


def main():
    print(three_sum_closest([-2, 0, 1, 2], 2))
    print(three_sum_closest([-3, -1, 1, 2], 1))
    print(three_sum_closest([1, 0, 1, 1], 100))


main()