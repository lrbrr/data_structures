class Solution:
    def romanToInt(self, s: str) -> int:
        roman_literals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        roman_values = [1, 5, 10, 50, 100, 500, 1000]
        
        to_find = [char for char in s]
        
        result = 0
        for i in range(len(to_find) - 1):
            if roman_literals.index(to_find[i+1]) > roman_literals.index(to_find[i]):
                result -= roman_values[roman_literals.index(to_find[i])]
            else:
                result += roman_values[roman_literals.index(to_find[i])]
                
        result += roman_values[roman_literals.index(to_find[-1])]
        
        return result

class Solution2:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
        
        result = 0
        for i in range(len(s) - 1):
            if romans[s[i]] < romans[s[i+1]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]

        return result + romans[s[-1]]

print(Solution().romanToInt('III')) # 3
print(Solution().romanToInt('LVIII')) # 58
print(Solution().romanToInt('MCMXCIV')) # 1994

print('-' * 50)

print(Solution2().romanToInt('III')) # 3
print(Solution2().romanToInt('LVIII')) # 58
print(Solution2().romanToInt('MCMXCIV')) # 1994