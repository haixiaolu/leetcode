"""
To calculate the maximum depth of the tree, we can recursively calculate its left and right subtree's maximum depth,
and then calculate current tree's max depth in O(1) time

- the base case for recursion is if th node is empty, then stop
"""
import collections


class Solution:
    def maxDepth(self, root):
        # DFS
        # if not root:
        #     return 0

        # else:
        #     left_height = self.maxDepth(root.left)
        #     right_height = self.maxDepth(root.right)

        #     return max(left_height, right_height) + 1

        # BFS
        """
        We need to pop all the nodes to extend which guaranted after each extend we have all the nodes in the queue
        """
        if root is None:
            return 0

        queue = collections.deque()
        queue.append(root)
        ans = 0
        while queue:
            currentSize = len(queue)
            for _ in range(currentSize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += 1
        return ans
