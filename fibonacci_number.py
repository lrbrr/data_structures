class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

class Solution2:
    def fib(self, n: int) -> int:
        result = [0, 1]
        for i in range(1, n):
            result.append(result[i] + result[i-1])
        return result[n]


print(Solution().fib(0)) # 0
print(Solution().fib(1)) # 1
print(Solution().fib(2)) # 1
print(Solution().fib(6)) # 8
print(Solution().fib(30)) # 832040

print( ' - ' * 20)

print(Solution2().fib(0)) # 0
print(Solution2().fib(1)) # 1
print(Solution2().fib(2)) # 1
print(Solution2().fib(6)) # 8
print(Solution2().fib(30)) # 832040