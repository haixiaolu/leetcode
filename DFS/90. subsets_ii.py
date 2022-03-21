def subsetsWithDup(nums):
    res, path = [], []
    nums.sort()
    dfs(nums, 0, res, path)
    return res


def dfs(nums, index, res, path):
    res.append(list(path))
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        path.append(nums[i])
        dfs(nums.i + 1, res, path)
        path.pop()
