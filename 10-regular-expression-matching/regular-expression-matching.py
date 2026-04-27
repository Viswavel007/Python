class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            # Check if result is already cached
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: if we reach the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' wildcard logic
            if j + 1 < len(p) and p[j+1] == '*':
                # Two choices: 
                # 1. Use '*' as zero (skip it): dp(i, j + 2)
                # 2. Use '*' as one or more (if first_match): dp(i + 1, j)
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Regular matching logic
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)
