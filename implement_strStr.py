class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

print(Solution().strStr("hello", "ll")) # 2
print(Solution().strStr("aaaaa", "bba")) # -1
print(Solution().strStr("", "a")) # -1
print(Solution().strStr("a", "")) # 0
print(Solution().strStr("a", "a")) # 0
print(Solution().strStr("a", "b")) # -1