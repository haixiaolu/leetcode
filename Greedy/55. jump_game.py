"""
尽可能到达最远位置（贪心）
如果能到达某个位置， 那一定能到达它前面的位置
方法： 
    - 初始化最远位置为0， 然后遍历数组， 如果当前位置能到达， 并且当前位置 + 跳数 > 最远位置， 就更新最远位置， 最后比较最远位置和数组长度
"""


def canJump(nums):
    # 初始化当前能到达的最远位置
    max_i = 0
    # i, 为当前位置， jump是当前位置的跳数
    for i, jump in enumerate(nums):
        # 如果当前位置能到达， 并且当前位置 + 跳数  > max_i:
        if max_i >= i and i + jump > max_i:
            max_i = i + jump  # 更新最远能到达的位置
    return max_i >= i


# method 2:
"""
1. 如果某个作为起跳点的格子可以跳跃的距离是3， 那么表示后面3个格子都可以作为起跳点
2. 可以对每一个能作为起跳点的格子都尝试跳一次， 把能跳到最远的距离不断更新
3. 如果可以一直跳到最后， 就成功了
"""


def canJump(nums):
    num = 0
    for i in range(len(nums)):
        if i > num:
            return False
        num = max(num, i + nums[i])
    return True
