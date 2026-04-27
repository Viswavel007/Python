class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # dp[j] will store the number of distinct subsequences of t[j:] in s[i:]
        # Base case: There is 1 way to form an empty string t
        dp = [0] * (m + 1)
        dp[m] = 1
        
        # Iterate backwards through s
        for i in range(n - 1, -1, -1):
            # Iterate backwards through t to use the current row's values 
            # without overwriting what we need for the same row
            for j in range(m):
                if s[i] == t[j]:
                    # If characters match, we have two choices:
                    # 1. Use s[i] to match t[j] -> dp[j+1]
                    # 2. Skip s[i] and look for t[j] later -> dp[j] (current value)
                    dp[j] = dp[j] + dp[j + 1]
                else:
                    # If they don't match, we must skip s[i]
                    # dp[j] remains the same
                    pass
                    
        return dp[0]
