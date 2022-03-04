"""
按顺序遍历字符串s
- 1. re[i] += c: 把每个字符c填入对应行Si 
- 2. i += flag： 更新当前字符c对应的行索引
- 3. flag = -flag: 在达到z字形转折点时，执行反向
"""


def convert(s, numRows):
    if numRows == 1:
        return s
    re = [""] * numRows
    i, flag = 0, -1
    for c in s:
        re[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return "".join(re)


print(convert("PAYPALISHIRING", 3))
