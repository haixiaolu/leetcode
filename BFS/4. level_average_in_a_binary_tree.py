# leetcode 637. Average of levels in  Binary Tree
"""
Given a binary tree, populate an array to represent the average of all it's level
"""
"""
Approach:
It follows the "Binary Tree Level Order Traversal" Pattern
- The only difference will be that instead of keeping tack of all nodes of a level,
  we will only track the running sum of the values of all nodes in each level
- In the end, we will append the average of the current level to the result array
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        result = []
        if root is None:
            return result

        queue = collections.deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            levelSum = 0.0
            for _ in range(levelSize):
                currentNode = queue.popleft()
                levelSum += currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(levelSum / levelSize)
        return result
