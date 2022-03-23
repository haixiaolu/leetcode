def restoreIpAddresses(self, s):
    # Base case
    if not s or len(s) < 4:
        return []

    # 初始化结果列表
    res = []
    # dfs 递归， 需要传入字符s， 对s的分割次数（初始为0）， 划分的中间（最终）结果， 最终结果列表res
    self.dfs(s, 0, "", res)
    # 返回结果列表
    return res


# dfs 递归， s为目标字符串， idx为对s的分割次数（也是递归深度
# path为划分的中间结果字符串， res为结果列表
def dfs(self, s, idx, path, res):
    # 如果idx大于4， 那么说明字符串s已经被分割的次数大于4， 此时直接返回
    if idx > 4:
        return

    # 如果idx等于4， 那么还要继续判断递归传入的s是否已经为空， 如果s为空则说明
    # 字符串已经被完全分割为ip地址的形式
    if idx == 4 and not s:
        # 这里符合条件的path的形式是 ‘xxx.xxx.xxx.xxx',
        # 因此path[:-1]是为了舍弃最后 '.'字符
        res.append(path[:-1])
        return

    # 对s的下标进行遍历
    for i in range(len(s)):
        # 后面的if语句用于处理一下两种情况
        # 1. 当s的首字符为‘0’时， 可以直接将0存为ip地址中4个整数之一
        # 2. 当s的首字符不为0时， 需要保证s[:i + 1]处于ip地址整数的范围之内
        if s[: i + 1] == "0" or (s[0] != "0" and 0 < int(s[: i + 1]) < 256):
            # dfs递归调用的参数需要进行以下操作
            # 1. 将下标i之后的s[i + 1:]字符串作为新的s进行递归参数传入
            # 2. 分割次数 idx + 1
            # 3. 将中间字符串结果path后连接下标i之前的 s[: i + 1]字符串， 并在最后加入 '.'
            # 4. 结果列表res依然原封不动的传入下次递归
            self.dfs(s[i + 1 :], idx + 1, path + s[: i + 1] + ".", res)
