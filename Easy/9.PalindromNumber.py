"""
Question: Given an integer x, return true if x is palindrome integer
          An integer is a palindrome when it reads the same backward as forward
          For example, 121 is a palindrome while 123 is not
"""

"""
Approach: 反转一半数字 
          将数字本身反转， 然后将反转后的数字与原始数字进行比较， 如果它们时相同的， 那么这个数字就是回文。
          为了避免数字反转可能导致的溢出问题， 我们可以反转int数字的一半，如果该数字时回文， 其后半部分反转后
          因该与原始数字的前半部分相同

          example： 输入1221， 后半部分反转21为12， 并将其与前半部分12进行比较， 相同true， 否则false
"""


def isPalindrome(x: int) -> bool:

    # 特殊情况， 当 x < 0 时， x不是回文数
    # 同样的， 如果数字的最后一位时0， 为了使该数字为回文，
    # 则其第一位数字也应该是0， 只有0满足这一属性
    if x < 0 or (x > 0 and x % 10 == 0):
        return False

    result = 0
    while x > result:
        # % 10 将得到最后一位数字，
        # 最后一位数字乘以10加上倒数第二位，就是想要的反转数
        result = result * 10 + x % 10
        x = x // 10
    # 如果数字长度为奇数时， 我们可以通过result//10 去除处于中位的数字
    return True if (x == result or x == result // 10) else False


# Time: O(logn)， 对于每次迭代， 我们会将输入除以10， 因此为O(logn)
# Space: O(1), 我们只需要常数空间存放若干变量

obj = isPalindrome(x=-121)
print(obj)
