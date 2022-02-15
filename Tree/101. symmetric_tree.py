# 递归
def isSymmetric(root):
    if not root:
        return True

    def dfs(left, right):
        # 递归的终止条件是两个节点都为空
        # 或者两个节点中有一个为空
        # 或者两个节点的值不相等
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)


# 迭代
def isSummetric(root):
    if not root or not [root.left or root.right]:
        return True

    queue = [root.left, root.right]
    while queue:
        # 从队列中取出两个节点， 在比较这两个节点
        left = queue.pop(0)
        right = queue.pop(0)

        # 如果两个节点都为空就继续循环，两者有一个为空，则为False
        if left is None and right is None:
            continue
        elif left is None or right is None:
            return False
        if left.val != right.val:
            return False

        # 将左节点的左孩子，右节点的右孩子放入队列
        queue.append(left.left)
        queue.append(right.right)
        # 将左节点的左孩子，右节点的左孩子放入队列
        queue.append(left.right)
        queue.append(right.left)
    return True
