def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, columns = len(matrix), len(matrix[0])
    order = list()

    left, right, top, bottom = 0, columns - 1, 0, rows - 1
    while left <= right and top <= bottom:
        # from left to right
        for column in range(left, right + 1):
            order.append(matrix[top][column])
            # from top to bottom
        for row in range(top + 1, bottom + 1):
            order.append(matrix[row][right])

        if left < right and top < bottom:
            # from right to left
            for column in range(right - 1, left, -1):
                order.append(matrix[bottom][column])
            # from bottom to top
            for row in range(bottom, top, -1):
                order.append(matrix[row][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return order


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
obj = spiralOrder(matrix)
print(obj)