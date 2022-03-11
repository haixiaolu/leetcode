"""
1. 正向查找可到达的最大位置
    我们维护当前能够到达的最大下标位置， 记为边界， 从左到右遍历数组， 到达边界时， 更新边界并将跳跃次数增加1

    在遍历数组时， 我们不访问最后一个元素， 这是因为在访问最后一个元素之前， 我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置
    如果访问最后一个位置， 在边界正好为最后一个位置的情况下， 我们会增加一个【不必要的跳跃次数】因此我们不必要访问最后一个元素
"""


def jum(nums):
    n = len(nums)
    maxPos, end, step = 0, 0, 0
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
    return step
