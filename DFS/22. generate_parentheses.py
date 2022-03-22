"""
结论：
- 当前左右括号都有大于0个可以使用的时候， 才产生分支
- 产生左分支的时候， 只看当前是否还有左括号可以使用
- 产生右分支的时候， 还受到左分支的限制， 右边剩余可以使用的括号数量一定的在严格大于左边剩余的数量的时候， 才可以产生分支
- 在左边和右边剩余的括号数等于0的时候结算
"""


def generateParentheses(n):
    # 减法
    res = []
    cur_str = ""

    def dfs(cur_str, left, right):
        if left == 0 and right == 0:
            res.append(cur_str)
            return

        if right < left:
            return

        if left > 0:
            dfs(cur_str + "(", left - 1, right)

        if right > 0:
            dfs(cur_str + ")", right, right - 1)

    dfs(cur_str, n, n)
    return res


print(generateParentheses(n=1))