"""
找到树的最后一行，
- 找到哪一行的第一个节点
"""
import collections


def findBottomLeftValue(root):
    queue = collections.deque()
    queue.append(root)

    while queue:
        currentSize = len(queue)
        res = queue[0].val
        for _ in range(len(currentSize)):
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return res
