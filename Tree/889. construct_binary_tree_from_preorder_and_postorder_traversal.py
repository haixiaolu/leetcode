def constructFromPrePost(preorder, postorder):
    def dfs(pre, post):
        if not pre:
            return None

        # 数组长度为1时，直接返回即可
        if len(pre) == 1:
            return TreeNode(pre[0])

        # 根据前序数组的第一个元素， 创建根节点
        root = TreeNode(pre[0])

        # 根据前序数组的第二个元素， 确定后序数组左子树范围
        left_count = post.index(pre[1]) + 1

        # 递归指向前序数组左边，后序数组左边
        root.left = dfs(pre[1 : left_count + 1], post[:left_count])

        # 递归执行前序数组右边， 后序数组右边
        root.right = dfs(pre[left_count + 1 :], post[left_count:-1])
        return root

    return dfs(preorder, postorder)
