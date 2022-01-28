# leetcode 18.4sum
"""
Given an array of unsorted numbers and a target number, find all unique quadruplets
in it, whose sum is equal to the target number
"""


def fourSum(nums, target):
    nums.sort()
    quadruplets = []
    for i in range(0, len(nums) - 3):
        # skip same element to avoid duplicate quadruplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            # skip same element to avoid duplicate
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            search_pair(nums, target, i, j, quadruplets)

    return quadruplets


def search_pair(nums, target_sum, first, second, quadruplets):
    left = second + 1
    right = len(nums) - 1
    while left < right:
        quad_sum = nums[first] + nums[second] + nums[left] + nums[right]
        if quad_sum == target_sum:  # found the quadruplet
            quadruplets.append([nums[first], nums[second], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1  # skip same element to avoid duplicate

        elif quad_sum < target_sum:
            left += 1

        else:
            right -= 1


def main():
    print(fourSum([4, 1, 2, -1, 1, -3], 1))
    print(fourSum([2, 0, -1, 1, -2, 2], 2))


main()