"""
Question: given the root of a binary tree, check whether it is a mirror of itself(i.e., symmetric around its center

"""
"""
Approach: 1. 递归
            两个树在什么情况下互为镜像：
            - 它们的两个跟节点具有相同的值
            - 每个树的右子树都与另一个树镜像对称

         用递归： 通过【同步移动】两个指针的方法来遍历这棵树， p指针和q指针一开始都指向这棵树的根， 
                随后p右移时， q左移，p左移，q右移。 每次检查当前p和q节点的的值是否相等， 如果相等在判断左右子树是否对称
"""


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetric1(root.left, root.right)

    def isSymmetric1(self, t1, t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        elif t1.val != t2.val:
            return False
        return self.isSymmetric1(t1.left, t2.right) and self.isSymmetric1(
            t1.right, t2.left
        )


# Time: O(n) 遍历了整棵树
# Space: O(n)
