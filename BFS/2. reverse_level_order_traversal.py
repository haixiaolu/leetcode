# leetcode 107. Binary Tree level order traversal II
"""
given a binary tree, populate an array to represent its level-by-level traversal in reverse order. You should
populate the values of all nodes in each level from left to right in separate subarrays
"""
"""
Approach:
- It follows the "Binary Tree Level Order Traversal"
- The only difference will be that instead of appending the current level at the end, we will append the current level
  at the beginning of the result list. 
- It uses a double-ended queue(deque)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_bottom(self, root):
        result = deque()
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.appendleft(current_level)
        return result
