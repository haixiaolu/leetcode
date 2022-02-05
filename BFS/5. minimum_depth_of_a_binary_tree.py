# leetcode 111.Minimum Depth of Binary Tree
"""
find the minmim depth of a binary tree. The minimum depth is the number noedes along the shortest
path from the root node to the nearset leaf node
"""
"""
It follows the Binary Tree Level Order Traversal 
The only difference will be, instead of keping tracking of all the nodes in a level,
we will only track the depth of the tree
As soon as we find our first leaf node, that level will represent the minimum depth of the tree
"""
import collections


def minDepth(root):
    if root is None:
        return 0

    queue = collections.deque()
    queue.append(root)
    minimumTreeDepth = 0
    while queue:
        minimumTreeDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # check if this a leaf node
            if not currentNode.left and not currentNode.right:
                return minimumTreeDepth

            # insert the children or current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
