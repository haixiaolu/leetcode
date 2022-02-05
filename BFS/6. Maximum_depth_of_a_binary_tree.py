# leetcode 104: maximum depth of a binary tree
"""
Given a bianry tree, find its maximum depth(or height)
"""
"""
We will follow a similar approach, instead of returning as soon as we find a leaf node, we will keep
traversing for all the levels, incrementing maximumDepth each time we complete a level
"""
import collections


def maxDepth(root):
    if root is None:
        return 0

    queue = collections.deque()
    queue.append(root)
    maximumDepth = 0
    while queue:
        maximumDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.currentNode.right
    return maximumDepth