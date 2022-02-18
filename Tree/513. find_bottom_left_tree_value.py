"""
递归：
使用前序遍历， 然后记录深度最大的叶子结点， 此时就是树的最后一行最左边的值

迭代：
层次遍历， 只需要记录最后一行第一节点的数值
"""
import collections


def findBottomLeftValue(root):
    queue = collections.deque([root])
    # 记录层次
    ans = []
    while queue:
        currentSize = len(queue)
        ans = queue[0].val
        for _ in range(currentSize):
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return ans


# Time: O(n)
# Space: O(n)