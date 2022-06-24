from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 != 0:
                result.append('Fizz')
            elif i%5 == 0 and i%3 != 0:
                result.append('Buzz')
            elif i%3 == 0 and i%5 == 0:
                result.append('FizzBuzz')
            else:
                result.append(str(i))
        return result

print(Solution().fizzBuzz(1)) # [1]
print(Solution().fizzBuzz(2)) # [1, 2]
print(Solution().fizzBuzz(3)) # [1, 2, Fizz]
print(Solution().fizzBuzz(4)) # [1, 2, Fizz, 4]
print(Solution().fizzBuzz(5)) # [1, 2, Fizz, 4, Buzz]
print(Solution().fizzBuzz(6)) # [1, 2, Fizz, 4, Buzz, Fizz]
print(Solution().fizzBuzz(15)) # [1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz]