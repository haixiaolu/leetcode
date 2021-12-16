"""
Question: given an integer array nums where the elements are sorted in ascending order, 
          convert it to a height-balanced binary search tree

          A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs
          by more than one
"""

"""
Approach: 中序遍历： 总是选择中间位置左边的数字作为根节点
                   选择中间位置左边的数字作为根节点， 则根节点的下标为mid = (left + right) / 2, 此处的除法为整数除法
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


"""
2. 中序遍历： 总是选择中间位置右边的数字作为根节点
            选择中间位置右边的数字作为根节点，则根节点的下标为mid = (left + right + 1) / 2
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 中间靠右的节点作为根节点
            mid = (left + right + 1) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


# Time: O(n)
# Space: O(log n)