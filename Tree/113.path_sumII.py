"""
DFS, iterate every path from root to leaf
- when we traverse to the leaf node, and its path's sum is the same as target, we found the right path
"""
# def pathSum(root, targetSum):
# DFS
# res = []
# path = []

# def dfs(root, targetSum):
#     if not root:
#         return
#     path.append(root.val)
#     targetSum -= root.val
#     if not root.left and not root.right and targetSum == 0:
#         res.append(path[:]) # 复制所有路径？
#     dfs(root.left, targetSum)
#     dfs(root.right, targetSum)
#     path.pop()

# dfs(root, targetSum)
# return res

"""
traverse whole tree, when we traverse to the leaf node, and the pathSum is the same as the targe sum, we found the right one.

- for saving some space, wo use hashmap to record every node's parent node
    - if we find the right one every time, then we start from this node to iterate to partent node
    - this way we can reduction to the original one 
"""
# BFS
import collections


def pathSum(root, targetSum):
    res = []
    parent = collections.defaultdist(lambda: None)

    def getPath(node):
        temp = list()
        while node:
            temp.append(node.val)
            node = parent[node]
        res.append(temp[::-1])

    if not root:
        return res

    queue_node = collections.deque([root])
    queue_total = collections.deque([0])

    while queue_node:
        node = queue_node.popleft()
        rec = queue_total.popleft() + node.val

        if not node.left and not node.right:
            if rec == targetSum:
                getPath(node)
        else:
            if node.left:
                parent[node.left] = node
                queue_node.append(node.left)
                queue_total.append(rec)
            if node.right:
                parent[node.right] = node
                queue_node.append(node.right)
                queue_total.append(rec)
    return rec
