# top to bottom
def isBalanced(root):
    # top to bottom
    def height(root):
        if not root:
            return 0
        return max(height(root.left), height(root.right)) + 1

    if not root:
        return True
    return (
        abs(height(root.left) - height(root.right)) <= 1
        and isBalanced(root.left)
        and isBalanced(root.right)
    )


## Bottom to top
def isBalanced(root):
    def height(root):
        if not root:
            return 0

        leftHeight = height(root.left)
        rightHeight = height(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1

    return height(root) >= 0