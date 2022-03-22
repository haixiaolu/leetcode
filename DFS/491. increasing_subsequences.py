"""
Base: 路径大于2， 是否递增， 递增继续添加路径
backtrack: 遍历候选，判断候选在当前层是否用过了 nums[start_index : i ] 
"""


def findSubsequence(nums):
    results = []

    def backtrack(start_index, path):
        # base case
        if len(path) >= 2:
            if path[-1] >= path[-2]:
                results.append(path)
            else:
                return

        # backtrack
        for i in range(start_index, len(nums)):
            # 去重
            if nums[i] in nums[start_index:i]:
                continue
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return results
