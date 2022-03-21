def subsets(nums):
    n = len(nums)
    ans = []

    def dfs(start, path):
        # 列表构造方法和[:]都是属于浅复制
        # 若这里直接传path， 而path是一个可变列表， 那么path后面有变化， ans也会变化
        ans.append(path[:])
        for i in range(start, n):
            path.append(nums[i])
            dfs(i + 1, path)
            # 所有层的递归里的path都是同一个内存地址， 所以path.append(nums[i])变化后，
            # 会影响所有层递归里的path
            # 所以一定要先pop撤销刚才的选择， 在回到上层dfs函数
            path.pop()

    dfs(0, [])
    return ans
