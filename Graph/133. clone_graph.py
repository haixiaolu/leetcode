"""
Given a reference of a node in a connected undirected graph. Return a deep copy of the graph
"""
"""
Approach:
1. 需要从给定的节点出发， 进行【图的遍历】来知道图的结构以及对应节点的值
2. 因为无向图的特点， （A可以访问B， B也可以访问A）， 为了防止多次遍历同一个节点，陷入死循环。 需要用一种数据
    结构记录已经被克隆过的节点

DFS算法：
    1. 使用哈希表存储所有已经被访问和克隆的节点。哈希表中的key是原始图中的节点， value时克隆图中的对应节点
    2. 从给定节点开始遍历图， 如果某个节点已经被访问过， 则返回其克隆图中的对应节点
    3. 如果当前访问的节点不在哈希表中，则创建它的克隆节点并存储在哈希表中，
        注意：在进入递归之前，必须先创建克隆节点并保存在哈希表中，如果不保证这种顺序， 可能会在递归中再次遇到同一个节点
        再次遍历该节点，陷入死循环
    4. 递归调用每个节点的邻接点的数量，每一次调用返回其对应邻接点的克隆节点， 最终返回这些克隆邻接点的列表， 将其放入对应
       克隆节点的邻接表中， 这样就可以克隆给定的节点和其邻接点中
"""
from collections import deque
from turtle import clone


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return node

        # 如果该节点被访问过， 则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点， 注意到我为了深度拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


## BFS
"""
1. 哈希表存储所有已被访问和克隆过的节点。 key是原始图中的节点，value是克隆图中的节点
2. 将题目给定的节点添加到队列，克隆该节点并存储到哈希表中
3. 每次从队列首部取出一个节点，遍历该节点的所有邻接点， 如果某个临界点已经被访问， 则该邻接点一定在visited中
   并将邻接点添加到队列， 将克隆的邻接点添加到克隆对应节点的邻接表中， 
4. 重复上述操作指导队列为空，则整个遍历结束
"""


def cloneGraph(node):
    if not node:
        return node
    visited = {}

    # 将题目给定的节点添加到队列中
    queue = deque([node])
    # 克隆第一个节点并存储到哈希表中
    visited[node] = Node(node.val, [])

    # BFS
    while queue:
        # 取出队列的头节点
        n = queue.popleft()
        # 遍历该节点的邻居
        for neighbor in n.neighbors:
            if neighbor not in visited:
                # 如果没有被访问过，克隆并赋值到哈希表中
                visited[neighbor] = Node(neighbor.val, [])
                # 将邻居节点加入到队列中
                queue.append(neighbor)
            # 更新当前节点的邻居列表
            visited[n].neighbors.append(visited[neighbor])
    return visited[node]
