"""
- 模拟BFS， 方法是判断在每个腐烂橘子的四个方向傻姑娘是否有新鲜橘子， 如果有就腐烂它， 每腐烂一次时间加1， 
  并剔除新鲜集合里腐烂的橘子
- 当橘子全部腐烂时结束循环
实现：
    - 初始化队列
    - 最开始的坏橘子全部入队， 具体是橘子的坐标和time
    - 循环： 当队列不为空时， 先弹出队元素， 然后将这个元素能够腐烂的橘子全部入队
"""


def orangesRotting(grid):
    row, col, time = len(grid), len(grid[0]), 0
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    queue = []

    # add the rotten oranges to the queue
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2:
                queue.append((i, j, time))

    # bfs
    while queue:
        i, j, time = queue.pop(0)
        for di, dj in directions:
            if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                grid[i + di][j + dj] = 2
                queue.append((i + di, j + dj, time + 1))

    # if there are still fresh oranges, return -1
    for row in grid:
        if 1 in row:
            return -1
    return time
