# leetcode 103.Binary Tree ZigZag Level Order Traversal
"""
Given a binary tree, populate an array to represent its zigzag level order traversal. You shoud populate
the values of all nodes of the first level from left to right, then right to left for the next level, and keep
alternating in the same manner for the following levels
"""
"""
Approach:
- it follows "Binary Tree Level Order Traversal" pattern
- The only addition step:
    -- we have to keep in mind is to alternate the level order traversal, which means that for every other level, we will traversal
       similar to Reverse Level Order Traversal 
"""
import collections
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzag_level_order(self, root):
        result = []
        if root is None:
            return result

        queue = collections.deque()
        queue.append(root)
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = deque()
            for _ in range(level_size):
                current_node = queue.popleft()
                # add the node to the current level based on the traverse direction
                if left_to_right:
                    current_level.append(current_node.val)
                else:
                    current_level.appendleft(current_node.val)
                # insert the children of current node in the queue
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(list(current_level))
            # reverse the traversal direction
            left_to_right = not left_to_right
        return result
