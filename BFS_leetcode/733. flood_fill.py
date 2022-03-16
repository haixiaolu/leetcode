"""
- 首先找到初始节点， 给它染色， 这个初始节点当作第一层
- 找到初始节点周围4个节点， 给他们染色（符合条件的才能染）， 这四个节点当作第二层
- 在找到这4个节点周围八个节点， 给他们染色， 这八个节点当作第3层
- 重复以往， 层层递进， 直到找不到符合要求的节点
"""
from queue import Queue


def floodFill(image, sr, sc, newColor):
    # 起始颜色和目标颜色相同， 则直接返回原图
    if newColor == image[sr][sc]:
        return image

    # 设置四个方向， （一种常见的省事儿技巧）
    directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    # 构造一个队列， 先把起始点放进去
    queue = Queue()
    queue.put((sr, sc))
    # 记录初始颜色
    orgColor = image[sr][sc]
    # 当队列不为空时
    while not queue.empty():
        # 取出队列点并染色
        point = queue.get()
        image[point[0]][point[1]] = newColor
        # 遍历四个方向
        for direction in directions:
            # 新点事new_i, new_j
            new_i = point[0] + direction[0]
            new_j = point[1] + direction[1]
            # 如果这个点在定义域内并且他和原来的颜色相同
            if (
                0 <= new_i < len(image)
                and 0 <= new_j < len(image[0])
                and image[new_i][new_j] == orgColor
            ):
                queue.put((new_i, new_j))
    return image
