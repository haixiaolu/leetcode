"""
Question: given a non-negative integer x, compute and return the square root of x
          since the return type is an integer, the decimal digits are truncated, 
          and only the integer part of the result is returned. 

          Note: you are not allowed to use any build-in exponent function or operator 

          Input: x = 4 Output: 2
"""
"""
Approach: 由于x平方根的整数部分ans是满足K^2 <= x的最大k值， 因此我们可以对k进行二分查找， 从而得到答案

          二分查找的下界为0， 上界可以粗略的设定为x， 在二分查找的每一步中， 我们只需要比较中间元素mid的平方与x的大小关系，
          并通过比较的结果调整上下界的范围。 由于我们所有的运算都是整数运算， 不会存在误差， 因此在得到最终答案ans后， 也就不需要再去尝试ans + 1了

        2. 牛顿迭代法
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, -1

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


# Time: O(log x)
# Space: O(1)