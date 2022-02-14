"""
在中序遍历中【定位】到根节点，那么分别知道左子树和右子树中的节点数目。 由于同一颗子树的前序遍历和中序遍历的长度显然是相同同的。
因此可以对应到前序遍历的结果中，对上述形式中的所有左右括号进行定位。
这样以来，我们就知道了左子树的前序遍历和中序遍历结果， 以及右子树的前序遍历和中序遍历的结果， 我们就可以递归的构造出左子树和右子树。
再将这两颗子树连接到根节点的左右位置

使用哈希表来帮助我们快速的定位根节点， 对于哈希映射中的每个键值对， 键表示一个元素（节点的值）， 值表示其在中序遍历中的出现位置
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(preorder, inorder):
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            # 前序遍历的第一个节点就是跟节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归构造左子树，并连接到根节点
            # 前序遍历中， 【从左边界 + 1 开始的size_left_subtee]个元素就对应了中序遍历
            # 【从左边界开始到根节点定位-1】的元素
            root.left = myBuildTree(
                preorder_left + 1,
                preorder_left + size_left_subtree,
                inorder_left,
                inorder_root - 1,
            )
            # 递归地构造右子树， 并连接到根节点
            # # 先序遍历中【从左边界+1 + 左子树节点数目开始到右边界】的元素就对应了中序遍历中【从根节点定位+1到右边界】的元素
            root.right = myBuildTree(
                preorder_left + size_left_subtree + 1,
                preorder_right,
                inorder_root + 1,
                inorder_right,
            )
            return root

        n = len(preorder)
        # 构造哈希映射， 帮组我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)
