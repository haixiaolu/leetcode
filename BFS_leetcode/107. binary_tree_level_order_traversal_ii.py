from asyncio import current_task
import collections


def levelOrderBottom(root):
    result = collections.deque()
    if root is None:
        return result

    queue = collections.deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(len(levelSize)):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(currentLevel)  # or result.append(currentLevel)

    return result  # or reversed(result)
