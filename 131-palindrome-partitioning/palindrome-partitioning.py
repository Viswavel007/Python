class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):
            # Base Case: If we've reached the end of the string
            if i >= len(s):
                res.append(part[:])
                return

            # Explore all possible substrings starting from index i
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    # If s[i:j+1] is a palindrome, add it and move forward
                    part.append(s[i : j + 1])
                    backtrack(j + 1)
                    # Backtrack: remove the last added substring
                    part.pop()

        backtrack(0)
        return res

    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
