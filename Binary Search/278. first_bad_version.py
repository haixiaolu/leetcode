"""
1. 将左右边界分别初始化为1和n， 其中n是给定的版本数量
2. 设定左右边界之后， 每次我们都依据左右边界找到其中间的版本，检查其是否为正确的版本
    - 如果该版本为正确的版本， 那么第一个错误的版本必然位于该版本的右侧，我们缩进左边界
    - 否则第一个错误的版本必然位于该版本的左侧，我们缩进右边界
3. 这样， 我们每判断一次都缩进一次边界， 而每次缩进时两边界距离将变为原来的一半
"""


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # 答案在【left, mid】之间
            else:
                left = mid + 1  # 答案在【mid+1, right】之间

        # 此时， left == right, 区间缩小一个点， 即为
        return left