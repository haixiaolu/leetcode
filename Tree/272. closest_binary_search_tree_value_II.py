"""
先中序遍历得到升序数组， 然后问题变成在一个升序数组里找最近target的k个值
问最接近/最大/最小的k个值问题， 就上【堆】
这里问最接近target， 就是问差值的绝对最小值， 所有开一个size为k的最大堆
"""
from heapq import *


def closestKValue(root, target, k):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    left = inorder(root)
    subs = []
    heapify(subs)
    for num in left:
        sub = abs(target - num)
        heappush(subs, (-sub, num))
        if len(subs) > k:
            heappop(subs)

    res = []
    for sub, num in subs:
        res.append(num)
    return res
