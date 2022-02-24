"""
1. 哈希表
枚举数组中的每个数x， 由于我们要枚举的数x一定是在数组中不存在前驱数x-1的， 因此我们每次在哈希表中检查是否
存在x-1即能判断是否需要跳过
"""


def longestConsecutive(nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        # 看当前数前面的数
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # 看当前数后面的数
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)
    return longest_streak