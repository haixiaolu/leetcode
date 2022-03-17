"""
每一次是原数字减去一个平方数， 直到出现第一个0， 此时走过的层数就是最小数量， 即为答案
"""


def numSquares(n):
    # 存储在n范围内的完全平方数
    squares = [i * i for i in range(int(n ** 0.5) + 1)]
    visited = set()  # 存储之前出现过的结果， 为了剪枝
    queue = [n]
    count = 0  # 当前层数
    while queue:
        # 这里类似于二叉树的层次遍历
        for _ in range(len(queue)):
            curr = queue.pop(0)
            # 当前节点值为0， 返回结果
            if curr == 0:
                return count

            for s in squares:
                res = curr - s
                if res >= 0 and res not in visited:
                    queue.append(res)
                    visited.add(res)
        count += 1