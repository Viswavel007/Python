class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case for 32-bit signed integers
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # Exponentially subtract divisor from dividend
        while a >= b:
            temp_divisor, count = b, 1
            # Double the divisor until it's larger than the remaining dividend
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            
            a -= temp_divisor
            res += count
            
        return -res if negative else res
