import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers to pick from: [1, 2, 3, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # k is 1-indexed in the problem, convert to 0-indexed for calculations
        k -= 1
        
        res = []
        
        # We determine each digit from left to right
        for i in range(n, 0, -1):
            # Calculate (i-1)! - how many permutations per digit choice
            factorial = math.factorial(i - 1)
            
            # Find the index of the current number to use
            idx = k // factorial
            res.append(numbers.pop(idx))
            
            # Update k for the next position
            k %= factorial
            
        return "".join(res)
