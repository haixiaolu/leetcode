"""
后序遍历和前序遍历
"""


def serialize(root):
    def postorder(root):
        return postorder(root.left) + postorder(root.right) + [root.val] if root else []

    return " ".join(map(str, postorder(root)))


def deserialize(data):
    def helper(lower=float("-inf"), upper=float("inf")):
        if not data or data[-1] < lower or data[-1] > upper:
            return None

        val = data.pop()
        root = TreeNode(val)
        root.right = helper(val, upper)
        root.left = helper(lower, val)
        return root

    data = [int(x) for x in data.split(" ") if x]
    return helper()