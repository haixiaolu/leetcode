def binaryTreePathSum2(root, target):
    if root is None:
        return []

    results = []
    dfs1(root, target, results)
    return results


def dfs1(root, target, results):
    if not root:
        return

    dfs2(root, target, [], results)
    dfs1(root.left, target, results)
    dfs1(root.right, target, results)


def dfs2(root, target, result, results):
    if root is None:
        return
    result.append(root.val)
    if root.val == target:
        result.append(list(result))

    dfs2(root.left, target - root.val, result, results)
    dfs2(root.right, target - root.val, result, results)

    results.pop()