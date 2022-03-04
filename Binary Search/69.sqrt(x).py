"""
由于x平方根的整数部分ans是满足 k^2 <= x的最大k值，因此我们可以对k进行二分查找，从而求出结果。
- 二分查找的下界为0， 上界可以粗略地设定为x， 在二分查找的每一步中， 我们只需要比较中间元素mid的平方与x的大小关系， 并通比较的结构调整上下界的范围
   - 由于所有的运算都是整数运算， 不会存在余差， 因此在得到最终的答案后，也就不需要在去尝试ans + 1 或者 ans - 1了
"""


def mySqrt(x):
    left, right, ans = 0, x, -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


print(mySqrt(4))