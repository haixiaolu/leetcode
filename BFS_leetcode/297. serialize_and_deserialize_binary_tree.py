"""
1. Serialize
    标准的 BFS Traversal
    需要注意的是， null也要加进去
2. Deserialize:
    - BFS的逆运算， 用(queue存放有parent的nodes， data存放没有parent的node)
    - 每次从queue里取出一个node， 就从data里取出最左边的两个座位left and right children 
    - 不断循环直到data为空
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root):
        from collections import deque

        # edge case
        # if root is None, return empty string
        if not root:
            return ""
        res = []
        queue = deque()
        queue.append(root)

        # keep traversal until queue is empty
        while queue:
            # 最左边的元素拿出来
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            # 如果node为空
            else:
                res.append("")
        # 最后把叶子结点的空（null） 去掉， 最右边的空节点去掉
        while res and res[-1] == "":
            res.pop()

        res = ",".join(res)
        return res

    def deserialize(self, data):
        from collections import deque

        if data == "":
            return None

        # convert the string to List[TreeNode]
        data = deque([TreeNode(int(i)) if i != "" else None for i in data.split(",")])

        # 不断从list的左边取元素， queue从左边取元素是O(1)
        root = data.popleft()
        queue = deque([root])
        while data:
            node = queue.popleft()
            node.left = data.popleft() if data else None
            node.right = data.popleft() if data else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
