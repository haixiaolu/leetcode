"""
- 在图中从顶点A到顶点B有一条有向路径， 则顶点A一定排在顶点B之前， 满足这样的条件的顶点序列称为一个拓扑序
- 拓扑排序有2个步骤：
    - 从队列中获取一个入度为0的顶点
    - 获取该顶点边， 将边的另一端入度减一， 如果为0， 也入队列
- 重复步骤1和2， 直到队列为空， 得到的出对顺序即为一个合理的拓扑排序
"""


import collections


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def topSort(self, graph):
        topo = []
        # indegree， 记录节点的入度
        in_degree = {}
        queue = collections.deque()
        for e in graph:
            for i in e.neighbors:
                # 记录每个节点的深度
                if i in in_degree:
                    in_degree[i] += 1
                else:
                    in_degree[i] = 1
        for e in graph:
            # 入度为0的作为起始点
            if e not in in_degree:
                queue.append(e)

        while len(queue) > 0:
            now = queue.popleft()
            topo.append(now)
            for e in now.neighbors:
                in_degree[e] -= 1
                if in_degree[e] == 0:
                    queue.append(e)
        return topo
