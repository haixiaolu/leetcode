"""
后序遍历最后一个元素代表的即为根节点，知道这个性质后，我们可以利用已知的根节点信息在中序遍历的数组中找到根节点所在的下标
然后根据其将中序遍历的数组分成左右两个部分， 左边部分即为左子树，右边部分为右子树，针对每个部分可以用同样的方法继续递归下去构造
"""
from logging.config import valid_ident


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(inorder, postorder):
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树， 就结束
            if in_left > in_right:
                return None

            # 选择post_index位置元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据root所在的位置分左右两颗子树
            index = idx_map[val]

            # 构造右子树
            root.right = helper[index + 1, in_right]

            # 构造左子树
            root.left = help[in_left, index - 1]

        # 建立（元素， 下标）键值对的哈希表
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
