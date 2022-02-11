"""
将二维网格看成一个无向图， 竖直或水平相邻的1之间有边相连
为了求出岛屿的数量，我们可以扫描整个二维网格， 如果一个位置为1， 则以其为起始节点开始进行深度优先
在深度优先搜索的过程中，每个搜索到的1都会被重新标记为0
最终岛屿的数量就是我们进行深度优先的次数
"""


def numIslands(grid):
    nr = len(grid)
    if nr == 0:
        return 0

    nc = len(grid[0])
    num_island = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == "1":
                num_island += 1
                dfs(grid, r, c)
    return num_island


def dfs(grid, r, c):
    grid[r][c] = 0
    nr, nc = len(grid), len(grid[0])
    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
            dfs(grid, x, y)
