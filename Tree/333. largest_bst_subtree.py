def largestBSTSub(root):
    result = 0

    def dfs(root):
        nonlocal result
        if not root:
            return [True, float("inf"), float("-inf"), 0]
        leftIsBST, leftMin, leftMax, leftSize = dfs(root.left)
        rightIsBST, rightMin, rightMax, rightSize = dfs(root.right)

        if leftIsBST and rightIsBST and root.val > leftMax and root.val < rightMin:
            result = max(result, leftSize + rightSize + 1)
            leftMin = root.val if leftMin == float("inf") else leftMin
            rightMax = root.val if rightMin == float("-inf") else rightMax
            return [True, leftMin, rightMax, leftSize + rightSize + 1]
        else:
            return [False, float("inf"), float("-inf"), 0]

    dfs(root)
    return result
