"""
- 如果当前节点不是叶子结点， 则在当前路径末尾添加该节点， 并继续递归遍历该节点的每一个孩子的节点
- 如果当前节点是叶子结点， 则在当前路径末尾添加该节点后就能得到一条从根节点到叶子结点的路径， 将该路径加入到答案即可
"""


class Solution:
    def binaryTreePaths(root):
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # leaf node
                    paths.append(path)

                else:
                    path += "->"  # not leaf node
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, "")
        return paths
