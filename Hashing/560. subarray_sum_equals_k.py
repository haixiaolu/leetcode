# 前缀和 + 字典
"""
每次遇到“连续子数组的和”相关问题， 我们可以考虑前缀和是否能行
使用字典记录每个前缀和的出现次数， 依次遍历数组元素时， 我们只能看到前面的前缀和， 所以直接相加即可
"""
import collections


def subarraySum(nums, k):
    presum_map = collections.defaultdict(int)
    presum_map[0] = 1
    presum, ans = 0, 0

    for i in range(len(nums)):
        presum += nums[i]
        target = presum - k
        if target in presum_map:
            ans += presum_map[target]
        presum_map[presum] += 1
    return ans
