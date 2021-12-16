"""
Question: Given the root of a binary tree, return the inorder traversal of its nodes' values
          Input: root = [1, null, 2, 3]  Output: [1, 3, 2]
"""
"""
中序遍历： 左子树 -> 根节点 -> 右子树
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        while stack or root:
            # 不断往左子树走，每走一次就将当前节点保存到栈中
            if root:
                stack.append(root)
                root = root.left

            # 当前节点为空， 说明左子树走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面操作
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res
