class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0: return s+t
        
        for char in s:
            t = t.replace(char, '', 1)
                
        return t

print(Solution().findTheDifference("abcd", "abcde")) # e
print(Solution().findTheDifference("", "a")) # a
print(Solution().findTheDifference("a", "")) # a
print(Solution().findTheDifference("a", "a")) # ''
print(Solution().findTheDifference("a", "ab")) # b