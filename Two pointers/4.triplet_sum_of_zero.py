# leetcode 15.3sum
"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero
"""


def threeSum(nums):
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # skip same element to avoid duplicate
            continue
        seach_pair(nums, -nums[i], i + 1, triplets)

    return triplets


def seach_pair(nums, target_sum, left, triplets):
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target_sum:  # found the triplets
            triplets.append([-target_sum, nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1  # skip sam element to avodid duplicate triplets
            while left < right and nums[right] == nums[right + 1]:
                right -= 1  # skip same element
        elif current_sum < target_sum:
            left += 1  # need a pair with a bigger sum
        else:
            right -= 1  # need a pair with a smaller sum


def main():
    print(threeSum([-3, 0, 1, 2, -1, 1, -2]))


main()