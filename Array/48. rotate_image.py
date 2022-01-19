# 先把二维矩阵沿对角线反转， 然后反转矩阵的每一行， 记过就是顺时针反转整个矩阵
def rotate(matrix):
    n = len(matrix)

    # 水平翻转
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i]

    # 主角线翻转
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]