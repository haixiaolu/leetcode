"""
我们需要求解的不仅仅是数字， 而是要求解所有的组合， 我们假设问题 f(1,n)是求解1到n（两端包含）的所有二叉树， 那么我们的目标就是求解f(1, n)

我们将问题进一步划分为子问题， 加入左侧和右侧的树分别求好了， 我们是不是只要运用组合的原理， 将左右两者进行合并就好了。 我们需要两层循环来完成这个问题
"""


def generateTrees(n):
    if not n:
        return []

    def generateTree(start, end):
        if start > end:
            return [None]

        res = []
        for i in range(start, end + 1):
            ls = generateTree(start, i - 1)
            rs = generateTree(i + 1, end)

            for l in ls:
                for r in rs:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res

    return generateTree(1, n)
