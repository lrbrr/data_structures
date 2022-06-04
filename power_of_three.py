class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n /= 3
        if n == 1:
            return True
        else:
            return False

print(Solution().isPowerOfThree(27)) # True
print(Solution().isPowerOfThree(0)) # False
print(Solution().isPowerOfThree(9)) # True
print(Solution().isPowerOfThree(45)) # False