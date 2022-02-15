"""
- 最左肯定最小 
- 由小到达遍历BST（in-order)
- 如果目前点比p点大， 那就往左看，因为右一定比p点还大，或者如果左是空，那么return root， 因为L -> Root -> R
- 不然就往右看
"""


def inorderSuccessor(root, p):
    def helper(node, p):
        if not node:
            return

        if node.val > p:
            return help(node.left, p) or node
        else:
            return helper(node.right, p)

    return helper(root, p)


# Follow up, use O(1) space
def inorderSuccessor(root, p):
    ans = None
    while root:
        if root.val > p:
            ans = root
            root = root.left
        else:
            root = root.right
    return ans
