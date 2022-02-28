"""
扫描整个网格， 如果一个位置为1， 则将其与相邻四个方向上的1在并查集中进行合并，最终岛屿数量即为并查集中联通分量的数目
"""


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i > 0 and grid[i - 1][j] == "1":
                        uf.union(i * n + j, (i - 1) * n + j)
                    if j > 0 and grid[i][j - 1] == "1":
                        uf.union(i * n + j, i * n + j - 1)
        return uf.getCount()


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

obj = Solution()
print(obj.numIslands(grid))