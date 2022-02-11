def preorderTraversal(root):
    res = []
    if not root:
        return res

    stack = []
    node = root
    while stack or root:
        while node:
            res.append(root)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = root.right
    return res

    # method 2 递归
    res = []

    def dfs(root):
        if root is not None:
            res.append(root)
            dfs(root.left)
            dfs(root.right)

    dfs(root)
    return res
