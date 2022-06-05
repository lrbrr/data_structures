from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if len(strs) == 1: return strs[0]

        result = ''
        for char1, char2 in zip(min(strs), max(strs)):
            if char1 == char2:
                result += char1
            else:
                break
        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"])) # "fl"
print(Solution().longestCommonPrefix(["dog","racecar","car"])) # ""
print(Solution().longestCommonPrefix(["a"])) # "a"
print(Solution().longestCommonPrefix([""])) # ""
print(Solution().longestCommonPrefix(["a",""])) # ""
print(Solution().longestCommonPrefix(["","a"])) # ""
print(Solution().longestCommonPrefix(["a","a"])) # "a"