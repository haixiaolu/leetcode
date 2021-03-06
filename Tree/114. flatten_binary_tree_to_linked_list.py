"""
前序遍历
"""


def flatten(root):
    preorderList = list()

    def preorderTraversal(root):
        if root:
            preorderList.append(root)
            preorderTraversal(root.left)
            preorderTraversal(root.right)

    preorderTraversal(root)
    size = len(preorderList)
    for i in range(1, size):
        prev, curr = preorderList[i - 1], preorderList[i]
        prev.left = None
        prev.right = curr


"""
迭代
"""


def flatten(root):
    preorderList = list()
    stack = list()
    node = root

    while node or stack:
        while node:
            preorderList.append(node)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    size = len(preorderList)
    for i in range(i, size):
        prev, curr = preorderList[i - 1], preorderList[i]
        prev.left = None
        prev.right = curr
