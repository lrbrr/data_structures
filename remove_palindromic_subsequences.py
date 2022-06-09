class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    def removePalindromeSub(self, s: str) -> int:
        return 1 if self.isPalindrome(s) else 2

print(Solution().removePalindromeSub("ababa")) # 1
print(Solution().removePalindromeSub("aaabbabab")) # 2