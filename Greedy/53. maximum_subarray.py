def maxSubarray(nums):
    # 类似寻找最大最小值的题目， 初始值一定要定义成理论上的最小最大值
    result = float("-inf")
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        result = max(result, cur_sum)
        # 如果cur_sum < 0, 重新开始找子序串
        if cur_sum < 0:
            cur_sum = 0
    return result


print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))