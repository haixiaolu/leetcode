import collections


def canFinish(numCourse, prerequisites):
    # 存储有向图
    edges = collections.defaultdict(list)
    # 存储每个节点的入度
    indegree = [0] * numCourse
    result = 0

    for info in prerequisites:
        edges[info[1]].append(info[0])
        indegree[info[0]] += 1

    q = collections.deque([u for u in range(numCourse) if indegree[u] == 0])
    while q:
        u = q.popleft()
        result += 1
        for v in edges[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return result == numCourse
