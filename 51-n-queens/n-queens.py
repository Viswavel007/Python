class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # Base Case: If we've placed queens in all rows, we found a solution
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # If the column or diagonals are occupied, skip this position
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # Move to the next row
                backtrack(r + 1)

                # Backtrack: Remove the queen and clean up sets
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
