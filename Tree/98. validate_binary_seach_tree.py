"""
中序遍历得到的值构成的序列一定是升级的

- 这启示我们在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可。
如果均大于说明这个序列是升序的。 整棵树是二叉搜索树， 否则不是
"""


def isValidBST(root):
    stack = []
    inorder = float("-inf")

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # 如果中序遍历得到的节点值小于等于前一个inorder， 不是二叉树
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return True
