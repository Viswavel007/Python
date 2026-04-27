class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # If this pair has been computed before, return the result
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        
        # Base cases
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2): # Quick pruning: if characters don't match
            self.memo[(s1, s2)] = False
            return False
            
        n = len(s1)
        # Try all possible split points
        for i in range(1, n):
            # Case 1: No swap at this split point
            # s1: [left][right], s2: [left][right]
            if (self.isScramble(s1[:i], s2[:i]) and 
                self.isScramble(s1[i:], s2[i:])):
                self.memo[(s1, s2)] = True
                return True
            
            # Case 2: Swapped at this split point
            # s1: [left][right], s2: [right][left]
            if (self.isScramble(s1[:i], s2[n-i:]) and 
                self.isScramble(s1[i:], s2[:n-i])):
                self.memo[(s1, s2)] = True
                return True
        
        self.memo[(s1, s2)] = False
        return False
