"""
Question: Given the root of a binary tree, return its maximum depth
          
          A binary tree's maximum depth is the number of nodes along the longest path from the root node 
          down to the farthest leaf node         
"""

"""
Approach: 深度优先搜索：
          如果我们知道左子树和右子树的最大深度l和r， 那么该二叉树的最大深度即为： max(l, r) + 1

          而左子树和右子树的最大深度有可以以同样的方式进行计算。 因此我们可以用【深度优先搜索】的方法来计算二叉树的最大深度。 
          具体而言， 在计算当前二叉树的最大深度时， 可以先递归计算出其左子树和右子树的最大深度， 
          然后在O(1)时间内计算出当前二叉树的最大深度， 递归到访问到空节点时推出
"""


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


# Time: O(n)
# Space: O(height)

"""
2. 广度优先搜索：
        广度优先需要修改一下： 
        - 广度优先搜索的队列里存放的时【当前层的所有节点】每次拓展下一层的时候， 不同于广度优先搜索的每次只从队列里拿出一个节点，
          我们需要将队列里的所有节点都拿出来进行拓展，这样能保证每次拓展完的时候队列里存放的是当前层的所有节点
        - 即我们是一层一层的进行拓展，最后我们用一个变量level来维护拓展的次数， 该二叉树的最大深度即为level
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        level = 0
        while queue:
            res = []
            for node in queue:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            queue = res
            level += 1
        return level
