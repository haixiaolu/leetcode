"""
1. 排序 + 贪心

为了尽可能满足最多数量的孩子， 从贪心的角度来考虑， 应该按照孩子的胃口从小到大的顺序一次满足每个孩子， 且对于每个孩子， 应该选择可以满足这个孩子
的胃口且尺寸最小的饼干
"""


def findContentChildren(g, s):
    count = 0
    kid, cookie = len(g) - 1, len(s) - 1
    g = sorted(g)
    s = sorted(s)

    while min(kid, cookie) >= 0:
        if g[kid] <= s[cookie]:
            count += 1
            cookie -= 1
        kid -= 1
    return count


print(findContentChildren([1, 2, 3], [1, 1]))