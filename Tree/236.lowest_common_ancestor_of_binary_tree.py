"""
若root是p， q的最近公共祖先， 则只能为以下情况之一：
1. p和q在root的子树中， 且分列root的两侧
2. p == root， 且q在root的左或右
3. q == root, 且p在root的左或右子树中
考虑通过递归对二叉树进行先序遍历，当遇到节点p或q时返回， 从底到顶回溯， 当节点p， q在节点root的异侧时， 
节点root即为最近公共祖先， 则向上返回
"""


def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left and not right:
        return
    if not left:
        return right
    if not right:
        return left
    return root
