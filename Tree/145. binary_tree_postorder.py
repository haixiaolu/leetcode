def postorderTraversal(root):
    res = []

    def dfs(root):

        if root is not None:
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

    dfs(root)
    return res

    # method 2 迭代
    res = []
    if not root:
        return res

    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            res.append(root.val)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right
    return res
