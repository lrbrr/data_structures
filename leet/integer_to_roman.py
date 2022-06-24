from unittest import result

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_literals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        roman_values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        
        i = 12
        result = ''
        while num:
            temp = num // roman_values[i]
            num = num % roman_values[i]
            
            while temp:
                result += roman_literals[i]
                temp -= 1
            i -= 1
        return result

class Solution2:
    def intToRoman(self, num: int) -> str:
        romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
        result = ''
        
        for i in romans:
            result += (num//i) * romans[i]
            num %= i
        
        return result

print(Solution().intToRoman(3)) # III
print(Solution().intToRoman(4)) # IV
print(Solution().intToRoman(9)) # IX
print(Solution().intToRoman(58)) # LVIII
print(Solution().intToRoman(1994)) # MCMXCIV
print(Solution().intToRoman(3999)) # MMMCMXCIX

print(' - '* 50)

print(Solution2().intToRoman(3)) # III
print(Solution2().intToRoman(4)) # IV
print(Solution2().intToRoman(9)) # IX
print(Solution2().intToRoman(58)) # LVIII
print(Solution2().intToRoman(1994)) # MCMXCIV
print(Solution2().intToRoman(3999)) # MMMCMXCIX