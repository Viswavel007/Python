class Solution(object):
    def reverse(self, x):
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            if res > (MAX_INT - pop) // 10:
                return 0
                
            res = res * 10 + pop
            
        return res * sign
