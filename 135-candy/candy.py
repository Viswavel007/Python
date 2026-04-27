class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # 1. Forward Pass: Check left neighbors
        # If a child has a higher rating than the one to the left, 
        # they must have more candies than that child.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # 2. Backward Pass: Check right neighbors
        # If a child has a higher rating than the one to the right, 
        # they must have more than that child, but we also respect 
        # the amount they already got from the forward pass.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
