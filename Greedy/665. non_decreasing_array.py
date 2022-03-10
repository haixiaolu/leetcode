"""
1. 如果当前数破坏了单调递增的话
    —— 我们修改他的前一个数， 因为我们也不知道当前数的后一个数是什么
    ——  或着修改前前个数
"""


def checkPossibility(nums):
    n = len(nums)
    count = 0
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            count += 1
            if i == 1 or nums[i] >= nums[i - 2]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
    return count <= 1