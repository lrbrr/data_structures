class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1, 1]
        for i in range(1, n):
            result.append(result[i] + result[i-1])
        return result[n]

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

print(Solution().climbStairs(1)) # 1
print(Solution().climbStairs(2)) # 2
print(Solution().climbStairs(5)) # 8
print(Solution().climbStairs(10)) # 89
print(Solution().climbStairs(45)) # 1836311903

print(' - ' * 50)

print(Solution2().climbStairs(1)) # 1
print(Solution2().climbStairs(2)) # 2
print(Solution2().climbStairs(5)) # 8
print(Solution2().climbStairs(10)) # 89
# print(Solution2().climbStairs(45)) # 1836311903 -> Time limit exceeds (Due to Recursion)