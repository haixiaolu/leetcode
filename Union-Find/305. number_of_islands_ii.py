class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0
        self.rank = []

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.root[root_x]
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            self.count -= 1

    def setParent(self, x):
        if self.parent.get(x):
            return
        self.parent[x] = x
        self.count += 1


class Solution:
    def numIslands2(self, m, n, position):
        """
        :type m: int
        :type n: int
        :type position: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind()
        uf.rank = [1] * (m * n)
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in position:
            index = x * n + y
            uf.setParent(index)
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < m and 0 <= new_y < n and new_x * n + new_y in uf.parent:
                    uf.union(index, new_x * n + new_y)
            res.append(uf.count)
        return res