# leetcode 199. Binary Tree Right Side View
"""
Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side
"""
"""
Approach:
It follows the 'Binary Tree level Order Traversal' pattern
The only additional thing we will be doing is to append the 
last node of each level to the result array
"""
import collections


def rightSideView(root):
    result = []
    if root is None:
        return result

    queue = collections.deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for i in range(0, levelSize):
            currentNode = queue.popleft()
            # if it is the last node of this level, add it to the result
            if i == levelSize - 1:
                result.append(currentNode.val)

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return result
