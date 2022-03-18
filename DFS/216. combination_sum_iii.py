"""
- 尝试减法， 减到0说明可能找到了一个符合题意的组合， 对组合里元素个数有限制， 对元素个数做判断
- 如果减到负数， 没有必要在继续搜索下去
- 结果集里的元素互不相同， 因此下一层搜索的起点应该是上一层搜索的起点值 + 1
"""


def combinationSum3(k, n):
    results = []

    def backtrack(remain, comb, next_state):
        if remain == 0 and len(comb) == k:
            # make a copy of current combination
            # otherwise the combination would be reverted in other branch of backtracking
            results.append(list(comb))
            return
        elif remain < 0 or len(comb) == k:
            # exceed the scope, no further explore
            return

        # iterate through the reduce list of candidates
        for i in range(next_state, 9):
            comb.append(i + 1)
            backtrack(remain - i - 1, comb, i + 1)
            # backtrack the current node
            comb.pop()

    backtrack(n, [], 0)
    return results


print(combinationSum3(k=3, n=7))
