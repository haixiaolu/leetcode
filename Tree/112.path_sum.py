"""
BFS, recored the path sum from root to current nodes
- To prevent repeate calculation, we can use two queues to store the nodes that we are going to traverse, and its path
  sum from root to these nodes
"""
import collections


def hasPathSum(root, targetSum) -> bool:
    # BFS
    # if root is None:
    #     return False

    # que_node = collections.deque([root])
    # que_value = collections.deque([root.val])

    # while que_node:
    #     cur = que_node.popleft()
    #     temp = que_value.popleft()
    #     if not cur.left and not cur.right:
    #         if temp == targetSum:
    #             return True
    #         continue
    #     if cur.left:
    #         que_node.append(cur.left)
    #         que_value.append(cur.left.val + temp)
    #     if cur.right:
    #         que_node.append(cur.right)
    #         que_value.append(cur.right.val + temp)
    # return False

    # 递归
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val

    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(
        root.right, targetSum - root.val
    )
