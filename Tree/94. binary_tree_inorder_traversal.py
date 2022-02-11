"""
Given the root of a binary tree, return the inorder traversal of its nodes'values
"""


def inorderTraversal(root):
    # method 1, 迭代
    res = []
    stack = []

    while stack or root:
        # 不断往左子树方向走，每走一次就将当前节点保存到栈中
        # 这是模拟递归的调用
        if root is not None:
            stack.append(root)
            root = root.left
        # 当前节点为空，说明左子树走到头了， 从 栈中弹出节点并保存
        # 然后转向右边节点， 继续上面流程
        else:
            temp = stack.pop()
            res.append(temp.val)
            root = temp.right
    return res


# method 2 递归
def inorderTraversal(root):
    result = []

    def inorder(root):
        if root is not None:
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

    inorder(root)
    return result
