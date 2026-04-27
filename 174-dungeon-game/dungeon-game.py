class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        
        # Initialize DP table with infinity
        dp = [[float('inf')] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Base case: health needed after reaching the princess is at least 1
        dp[ROWS][COLS - 1] = 1
        dp[ROWS - 1][COLS] = 1
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                # How much health do we need to have AFTER this cell?
                # We take the minimum of the paths below or to the right
                min_health_needed_after = min(dp[r + 1][c], dp[r][c + 1])
                
                # Health needed to enter this cell = needed_after - current_cell_value
                # If the result is <= 0 (due to big magic orbs), we still need 1 health to exist
                dp[r][c] = max(1, min_health_needed_after - dungeon[r][c])
                
        return dp[0][0]
