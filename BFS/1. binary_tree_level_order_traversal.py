# Leetcode 102. Binary Tree Level Order Traversal
"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes
of each level from left to right in separate sub-arrays
"""
"""
Approach:
Use a queue to efficiently traverse in BFS fashion
    - start by pushing the root node to the queue
    - keep iterating until the queue is empty
    - in each iteration, first count the elements in the queue(let's call it levelSize). We will have these many nodes in the current node
    - next, remove levelSize nodes from the queue and push their value in an array to represent the current level
    - after removing each node from the queue, insert both of its children into the queue
    - if the queue is not empty, repeat from step 3 for the next level 
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        result = []
        if root is None:
            return result

        # use a queue
        queue = collections.deque()
        # push the root node to the queue
        queue.append(root)
        # iterate until queue is empty
        while queue:
            # count the element in the queue
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                # remove levelSize node
                current_node = queue.popleft()
                # add the node to the current level
                current_level.append(current_node.val)
                # insert the children of current node in the queue
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_level)

        return result
