"""
对于数组中重复元素的情况： 
- 在无法判断区间的情况下， 我们缩进搜索空间， 左边界 + 1， 右边界 - 1
- 然后在新区间上继续二分搜索
"""


def search(nums, target):
    if not nums:
        return False

    n = len(nums)
    if n == 1:
        return nums[0] == target

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        # 缩进搜索空间
        if nums[left] == nums[mid] and nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


print(search([2, 5, 6, 0, 0, 1, 2], 0))