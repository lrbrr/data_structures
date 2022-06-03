class Solution:
    def mySqrt(self, x: int) -> int:
        estimate = 1
        while abs(estimate * estimate - x) > 0.001:
            estimate = (estimate + (x / estimate)) / 2
        
        return int(estimate)

print(Solution().mySqrt(8)) # 2
print(Solution().mySqrt(4)) # 2
print(Solution().mySqrt(1)) # 1
print(Solution().mySqrt(0)) # 0
print(Solution().mySqrt(2147395599)) # 46339
print(Solution().mySqrt(2147395600)) # 46340