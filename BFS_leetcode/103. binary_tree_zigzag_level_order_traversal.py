"""
follows the same pattern as [102.Binary Tree Level Order Traversal]
- The only additional step we have to keep in mind is to alternative the level order traversal,
  which means that for every other lever, we will traversal similar to [reverse level order traversal]
"""
import collections


def zigZagLevelOrder(root):
    result = []
    if not root:
        return result

    queue = collections.deque()
    queue.append(root)
    leftToRight = True
    while queue:
        levelSize = len(queue)
        currentLevel = collections.deque()
        for _ in range(len(levelSize)):
            currentNode = queue.popleft()

            # add the node to the current level based on the traverse directior
            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(list(currentLevel))
    # reverse the traversal direction
    leftToRight = not leftToRight
    return result
