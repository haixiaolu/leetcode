"""
主循环：
    - 遍历整个矩阵， 当遇到 grid[i][j] == '1' 时， 从此点开始BFS， 岛屿数 count + 1, 且在BFS中删除此岛屿
    - 最终返回岛屿数count即可
BFS：
    - 主循环
    - 借用一个队列queue， 判断队列首部节点（i， j）是否未越界且为1
        - 若是则置零（删除岛屿节点）， 并将此节点上下左右节点 (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)加入队列
        - 若不是则跳过

    - 循环pop队列首节点， 直到这个队列为空， 此时已经遍历完此岛屿
"""


def numIslands(grid):
    def bfs(grid, i, j):
        queue = [[i, j]]
        while queue:
            [i, j] = queue.pop(0)
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] == 0
                queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0":
                continue
            bfs(grid, i, j)
            count += 1
    return count
