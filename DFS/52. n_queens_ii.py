class Solution:
    def solverNQueens(self, n):
        columns = set()
        posDiag = set()
        negDiag = set()

        def backtrack(row):
            if row == n:
                return 1

            else:
                count = 0

                for col in range(n):
                    if (
                        col in columns
                        or (row + col) in posDiag
                        or (row - col) in negDiag
                    ):
                        continue

                    columns.add(col)
                    posDiag.add(row + col)
                    negDiag.add(row - col)
                    count += backtrack(row + 1)

                    columns.remove(col)
                    posDiag.remove(row + col)
                    negDiag.remove(row - col)

                return count

        return backtrack(0)


s = Solution()
print(s.solverNQueens(4))