class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            if num%2 == 0:
                num = num // 2
            else:
                num -= 1
        return count

class Solution2:
    def numberOfSteps (self, num: int) -> int:
        return bin(num).count("1") * 2 + bin(num).count("0") - 2

print(Solution().numberOfSteps(14)) # 6
print(Solution().numberOfSteps(8)) # 4
print(Solution().numberOfSteps(123)) # 12
print(Solution().numberOfSteps(0)) # 0
print(Solution().numberOfSteps(1)) # 1

print(' - ' * 50)

print(Solution2().numberOfSteps(14)) # 6
print(Solution2().numberOfSteps(8)) # 4
print(Solution2().numberOfSteps(123)) # 12
print(Solution2().numberOfSteps(0)) # 0
print(Solution2().numberOfSteps(1)) # 1