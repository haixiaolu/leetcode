"""
DFS
- 先把太平洋（左边界， 上边界） 和大西洋（右边界，下边界） 找出来
- 然后用DFS搜索能否到达， 如果碰到以搜索的节点， 停止搜索
- 题目要求水只能从高往低流， 所以如果两个目的地的边向外搜索的话， 必须是升序或者相等的
- 从上边界一直往下dfs， 看能都到达太平洋， 同理， 从下往上， 看能否到达大西洋
- 用hashset记录遍历过的节点， 避免重复
"""


def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prevHeight):
        if (
            (r, c) in visited
            or r < 0
            or c < 0
            or r == rows
            or c == cols
            or heights[r][c] < prevHeight
        ):
            return
        visited.add((r, c))
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    # go through first row
    for c in range(cols):
        dfs(0, c, pac, heights[0][c])  # first row of pac
        dfs(rows - 1, c, atl, heights[rows - 1][c])

    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols - 1, atl, heights[r][cols - 1])

    res = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res
