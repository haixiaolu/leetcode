"""
并查集模版
"""


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = 0

        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.size -= 1
            self.parent[root_x] = root_y


class Solution:
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[bool]]
        :rtype: int
        """
        if not isConnected:
            return 0
        m, n = len(isConnected), len(isConnected[0])
        uf = UnionFind(m)
        for i in range(m):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.size
