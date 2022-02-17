"""
DFS
- traverse the tree, and recored the depth 
- for every non-leaf node, only recored their left and right subtree's minimum depth
- this will divided into smaller problem
- use recursion to solve this problem 
"""
import collections
from numpy import BUFSIZE


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        # DFS
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1

        # min_depth = 10**9
        # if root.left:
        #     min_depth = min(self.minDepth(root.left), min_depth)
        # if root.right:
        #     min_depth = min(self.minDepth(root.right), min_depth)

        # return min_depth + 1

        # BFS
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0
