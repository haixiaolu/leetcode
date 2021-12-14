"""
Question: Given two binary strings a and b, return their sum as a binary string

Input: a = "11", b = "1"   Output: "100"
       a = "1010" b = "1011"  Output: 10101
"""
"""
Approach: 位运算
    - 如果不允许使用加减乘除， 则可以使用位运算替代加减乘除的操作， 
    - 我们可以设计这样的算法来计算：
        -- 把a和b转换成整型数字x和y， 在接下来的过程中， x保存结果，y要保存进位
        -- 当进位不为0时
            --- 计算当前x和y的无进位相加结果： answer = x ^ y
            --- 计算当前x和y的进位： carry = (x & y) << 1
            --- 完成本次循环， 更新 x = answer, y = carry
    - 返回x的二进制形式

    为什么这个方法可行呢？ 在第一轮计算中， answer的最后一位是x和y相加之后的结果，carry的倒数第二位是x和y最后一位相加的进位。 
    接着每一轮中， 由于carry是由x和y按位与并且左移得到的， 那么最后会补零， 所以在下面计算的过程中后面的数位不受影响， 而每一轮都可以得到一个低i
    位的答案和它向低i+1位的进位， 也就模拟了加法的过程。 
"""


class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


# Time: O(|a| + |b| + X.max(|a| + |b|))
# Space: O(|a| + |b|)


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = ""
        carry = 0

        # reverse
        a, b = a[::-1], b[::-1]

        # loop over the longest str
        for i in range(max(len(a), len(b))):
            # edge case of outbound
            # ord is converting char to int
            # if it's outbound, give it 0
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = total % 2  # base 2, if total = 3, % 2= 1
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res  # edge cases
