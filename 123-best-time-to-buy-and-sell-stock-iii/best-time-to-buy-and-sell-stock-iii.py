class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize states:
        # buy1/buy2: we want to minimize cost (maximize negative money)
        # sell1/sell2: we want to maximize profit
        buy1 = float('inf')
        sell1 = 0
        buy2 = float('inf')
        sell2 = 0
        
        for price in prices:
            # 1. Best price to buy the first stock (minimize cost)
            buy1 = min(buy1, price)
            
            # 2. Profit if we sell the first stock today
            sell1 = max(sell1, price - buy1)
            
            # 3. Best price to buy the second stock 
            # (effectively uses profit from sell1 to lower the cost of buy2)
            buy2 = min(buy2, price - sell1)
            
            # 4. Profit if we sell the second stock today
            sell2 = max(sell2, price - buy2)
            
        return sell2
