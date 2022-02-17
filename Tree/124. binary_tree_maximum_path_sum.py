"""
实现一个简化函数 maxGain(node)， 该函数计算二叉树中的一个节点的最大贡献值， 具体而言， 就是在以该节点为根节点的子树中寻找以该节点为
起点的一条路径， 使得该路径上的节点值之后最大
"""


class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root):
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于0时， 才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewPath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewPath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
