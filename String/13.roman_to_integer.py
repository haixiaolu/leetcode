"""
1. 模拟
 - 罗马数字中小的数字在大的数字的右边， 若输入的字符串满足该情况， 那么可以将每个字符视作一个单独的值， 累加每个字符对应的数值即可
 - 若存在小的数字在大的数字的左边， 根据规则需要减去小的数字 
    - 对于这种情况， 我们也可以将每个字符视作一个单独的值， 若一个数字右侧的数字比它大， 则将该数字的符号取反
 
"""


def romanToInt(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    i = 0
    while i < len(s):
        # if this is the subtractive case
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total += values[s[i + 1]] - values[s[i]]
            i += 2
        # else this is not the subtractive case
        else:
            total += values[s[i]]
            i += 1
    return total