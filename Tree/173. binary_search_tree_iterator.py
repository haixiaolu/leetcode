"""
迭代：
- 一路到底， 将根节点和它的所有节点放到栈中
- 调用next， 弹出栈顶的节点
-- 如果它有右子树， 则对右子树一路到底，把它和他的所有左节点放到栈中
"""


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        return len(self.stack) > 0
