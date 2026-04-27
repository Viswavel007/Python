class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a single row with 1s
        # (There's only 1 way to reach any cell in the first row)
        row = [1] * n
        
        # Iterate through the remaining m-1 rows
        for i in range(m - 1):
            new_row = [1] * n
            # Start from index 1 because the first column is always 1
            for j in range(1, n):
                # Ways to reach = Ways from above + Ways from left
                new_row[j] = new_row[j - 1] + row[j]
            row = new_row
            
        return row[-1]
