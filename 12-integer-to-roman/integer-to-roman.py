class Solution(object):
    def intToRoman(self, num):
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_parts = []
        
        for value, symbol in values:
            if num == 0: break
            count = num // value
            if count > 0:
                roman_parts.append(symbol * count)
                num -= value * count
                
        return "".join(roman_parts)
