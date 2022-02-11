"""
一.BFS
- 从start开始能够到达所有的位置，如果其中某个位置对应的元素值为0， 那么就返回True
具体的：
1. 我们初始时将start加入队列， 在每一次的搜索过程中，我们取出队首的节点u， 它可以到达的位置为 u + arr[u]和 u - arr[u].
2. 如果某个位置在数组的下标范围[0, len(arr)]内， 并且没有被搜过， 则将该位置加入队尾。
3. 只要搜索到一个对应元素值为0的位置，我们就返回True
4. 在搜索过程中， 如果仍然没有找到符合要求的位置， 我们就返回False

"""


import collections


def canReach(arr, start):
    if arr[start] == 0:
        return True

    n = len(arr)
    used = {start}
    q = collections.deque([start])

    while len(q) > 0:
        u = q.popleft()
        for v in [u + arr[u], u - arr[u]]:
            if 0 <= v < n and v not in used:
                if arr[v] == 0:
                    return True
                q.append(v)
                used.add(v)
    return False
