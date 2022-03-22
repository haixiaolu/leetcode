class Solution:
    def solverNQueens(self, n):
        columns = set()
        positiveDiag = set()  # row + col
        negativeDiag = set()  # row - col

        res = []
        board = [["."] * n for i in range(n)]  # create a board

        def backtrack(row):
            # base case
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # try every element in current row
            for col in range(n):
                if (
                    col in columns
                    or (row + col) in positiveDiag
                    or (row - col) in negativeDiag
                ):
                    continue

                columns.add(col)
                positiveDiag.add(row + col)
                negativeDiag.add(row - col)

                backtrack(row + 1)

                columns.remove(col)
                positiveDiag.remove(row + col)
                negativeDiag.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return res
