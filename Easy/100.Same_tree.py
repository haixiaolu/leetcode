"""
Question: Given the roots of two binary trees p and q, write a function to check if they are the same or not

          Two binary trees are considered the same if they are structurally identical, and the nodes have the same value 
"""
"""
Approach: 1. 深度优先搜索
             如果两个二叉树都为空， 则两个二叉树相同。 如果有且只有一个为空，则两个二叉树一定不相同
             - 如果两个二叉树都不为空：
                -- 首先判断它们的根节点的值是否相同， 
                    --- 若不相同，则两个二叉树一定不同
                    --- 若相同， 再分别判断两个二叉树的左子树是否相同以及右子树是否相同
             - 递归地判断两个二叉树是否相同
"""


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Time: O(min(m, n)) 其中m和n分别是两个二叉树的节点数。 对两个二叉树同时进行深度优先搜索，
#                    只有当两个二叉树中的对应节点都不为空时才会访问到该节点， 因此被访问到的节点数不会超过较小的二叉树的节点数

# Space: O(min(m, n)), 其中m和n分别是两个二叉树的节点数， 空间复杂度取决于递归调用的层数

"""
2. 广度优先搜索： 
        同样首先判断两个二叉树是否为空， 如果两个二叉树都不为空，则从两个二叉树的根节点开始广度优先搜索
        - 使用两个队列分别存储两个二叉树的节点。初始时将两个二叉树的根节点分别加入两个队列，每次从两个队列各取出一个节点， 进行如下比较：
            -- 比较两个节点的值，如果两个节点的值不相同则两个二叉树一定不同
            -- 如果两个节点的值相同，则判断两个节点的子节点是否为空，如果只有一个节点的左子节点为空，
            或者只有一个节点的右子节点为空， 则两个二叉树的结构不同， 因此两个二叉树一定不同
            -- 如果两个节点的子节点的结构相同，则将两个节点的非空子节点分别加入两个队列， 子节点加入队列时需要注意顺序，
               如果左右子节点都不为空，则先加入左子节点，后加入右子节点

"""


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False

            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(right1)
            if right2:
                queue2.append(right2)
        return not queue1 and not queue2


# Time: O(min(m, n))
# Space: O(min(m, n))