# leetcode 117.Populating next right pointers in each node II
"""
Given a binary tree, connect each node with its level order successor.
The last node of each level should point to a null node
"""
"""
It follows the 'Binary Tree Level Order Traversal' pattern
The only difference is that while traversing a level we will remember the previous node
to connect it with the current node
"""
import collections


def connect(root):
    if root is None:
        return
    queue = collections.deque()
    queue.append(root)
    while queue:
        previousNode = None
        levelSize = len(queue)
        # connect all nodes of this level
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode

            # insert children
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return root
