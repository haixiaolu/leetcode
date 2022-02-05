# geekforgeeks
"""
Given a binary tree and a node, find the level order successor of the given node in the tree.
The level order successor is the node that appears right 
after the given node in the level order traversal
"""
"""
Approach:
It follows the "Binary Tree Level Order Traversal" pattern
- The only difference will be that we will not keep track of all the levels. Instead 
  we will keep inserting child nodes to the queue
- As soon as we find the given node, we will return th next node from the queue  as the 
  level order successor
  - 1. at every step of the level order traversal, check if the current node matches with 
       the given node.
  - 2. if True, stop traversing any further and return the element at top of queue which
       will be the next node in the level order traversal
"""
import collections


def find_successor(root, key):
    if root is None:
        return None
    queue = collections.deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        # break if we have found the key
        if currentNode.val == key:
            break
    return queue[0] if queue else None
