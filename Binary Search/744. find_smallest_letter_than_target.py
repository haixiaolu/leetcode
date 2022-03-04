"""
1. Linear Scan
    Since letter are sorted, if we see something larger when scanning from left to right, it must be the answer. 
    Otherwise, the answer is letters[0]
"""


def nextGreatestLetter(letters, target):
    for c in letters:
        if c > target:
            return c
    return letters[0]


"""
2. Binary Search
当目标字母target比字符列表中的所有字母都大， 返回的是字符列表中的第一个字母， 否则返回的是letters[left], 所以可以将上一段代码优化一下，
采用取余运算。 
- 当left < letterSize时， left对letterSize取余， 结果是自身
- 当left == letterSize时， left对letterSize取余， 结果是0
"""


def nextGreatestLetter(letters, target):
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return letters[left % len(letters)]
