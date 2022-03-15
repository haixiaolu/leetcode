import collections


def hasPath(matrix, start, end):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # up, down, left, right
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    visited[start[0][start[1]]] = True

    q = collections.deque([start])
    while q:
        currentPath = q.popleft()
        if currentPath[0] == end[0] and currentPath[1] == end[1]:
            return True

    for dir in dirs:
        # roll the ball until it hits a wall
        row = currentPath[0] + dir[0]
        col = currentPath[1] + dir[1]

        while (
            0 <= row < len(matrix)
            and 0 <= col < len(matrix[0])
            and matrix[row][col] == 0
        ):
            row += dir[0]
            col += dir[1]

        # x and y locates at a wall when existing the above while loop, so we need to backtrack 1 position
        new_x, new_y = row - dir[0], col - dir[1]

        # check if the new starting position has been visited
        if not visited[new_x][new_y]:
            q.append((new_x), (new_y))
            visited[new_x, new_y] = True
    return False
