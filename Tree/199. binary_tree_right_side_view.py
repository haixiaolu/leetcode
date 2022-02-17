"""
DFS
先访问右子树， 那么对于每一层来说， 我们在这层见到的一个节点一定是最右边的结点
- 我们可以存储在每个深度访问的第一个结点， 一旦我们知道了树的层数， 就可以得到最终的结果数组
"""


def rightSideView(root):
    rightmost_value_at_depth = dict()  # 深度为索引， 存放节点的值
    max_depth = -1

    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        if node is not None:
            # 维护二叉树的最大深度
            max_depth = max(max_depth, depth)

            # 如果不存在对应深度的节点我们才插入
            rightmost_value_at_depth.setdefault(depth, node.val)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

    return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]