"""
题目给出了多个1， 要找出每个1到0的最近曼哈顿距离， 由于1到0的距离和0到1的距离一样， 所以其实我们可以换个思维， 找出每个0到1的距离 （多个起始点BFS）
剩下的任务就是套模版了
"""
import collections


def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])
    queue = collections.deque()
    visited = [[0] * cols for _ in range(rows)]
    res = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    step = 0
    while queue:
        size = len(queue)
        for i in range(size):
            x, y = queue.popleft()
            if mat[x][y] == 1:
                res[x][y] = step

            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if (
                    new_x < 0
                    or new_x >= rows
                    or new_y < 0
                    or new_y >= cols
                    or visited[new_x][new_y] == 1
                ):
                    continue
                queue.append((new_x, new_y))
                visited[new_x][new_y] = 1
        step += 1
    return res
