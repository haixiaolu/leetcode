"""
- 使用一个队列
- 开始时， 所有入度为0的节点都被放入到队列中， 它们就是可以作为拓扑排序最前面的节点， 并且它们之间的相对顺序是无关紧要的
- 在BFS的每一步中，我们取出队首的节点u
    - 将u放入答案中
    - 移除u的所有出边， 也就是将u的所有相邻节点的入度减少1， 如果某个相邻节点u的入度变为0， 那么就将u放入队列中
"""


def findOrder(numCourses, prerequisites):
    from collections import defaultdict, deque

    # 存储有向图
    edge = defaultdict(list)
    # 存储每个节点的入度
    indegree = [0] * numCourses
    # 存储答案
    result = []

    for info in prerequisites:
        edge[info[1]].append(info[0])
        indegree[info[0]] += 1

    # 将所有入度为0的节点放入队列中
    q = deque([u for u in range(numCourses) if indegree[u] == 0])

    while q:
        # 从队首取出一个节点
        u = q.popleft()
        # 放入答案中
        result.append(u)
        for v in edge(u):
            indegree[v] -= 1
            # 如果相邻节点v的入度为0， 就可以选v对应的课程了
            if indegree[v] == 0:
                q.append(v)
    if len(result) != numCourses:
        result = []
    return result