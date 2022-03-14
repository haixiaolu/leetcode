"""
1. 标准BFS
 - Initialize Queue qith all entry points
 - while queue is not empty:
    - for each node in qhe queue
    - pull out the element(add to result)
    - expand it, offer children to the queue inorder(左到右，或者右到左)
    - increase it 
"""
import collections


def leverOrder(root):
    if not root:
        return

    # 根节点
    queue = collections.deque([root])
    res = []
    while queue:
        res.append([node.val for node in queue])
        level = []
        # 对当前层每个节点遍历
        for node in queue:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        # 后把queue更新层下一层的终点， 继续遍历下一层
        queue = level
    return res
