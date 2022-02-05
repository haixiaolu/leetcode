# GeeksforGeeks
"""
Given the root to a binary tree where each node has an additional pointer called sibling(or next)
connect the sibling pointer to the next node in the same level. The last node in each level should
point to the first of the next level in the tree
"""
"""
It follows the 'Binary Tree Level Order Traversal' pattern
The only difference will be that while traversing we will remember (irrespective of the level) the 
previous node to connect it with the current node
"""
import collections


def connect_all_sibling(root):
    if root is None:
        return

    queue = collections.deque()
    queue.append(root)
    currentNode, previousNode = None, None
    while queue:
        currentNode = queue.popleft()
        if previousNode:
            previousNode.next = currentNode
        previousNode = currentNode

        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)