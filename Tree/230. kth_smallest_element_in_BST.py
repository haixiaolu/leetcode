"""
迭代：
中序遍历
"""


def kthSmallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
