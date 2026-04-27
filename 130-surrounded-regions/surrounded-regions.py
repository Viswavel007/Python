class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            # Mark the 'O' as temporary 'T' (Safe/Not surrounded)
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Start DFS from all 'O's on the border (top, bottom, left, right)
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == "O":
                    dfs(r, c)

        # 2. Process the whole board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X" # Surrounded -> Flip to X
                elif board[r][c] == "T":
                    board[r][c] = "O" # Safe -> Restore to O

        