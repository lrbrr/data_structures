class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        all_possible_substring = []
        substring = ''
        for char in s:
            if char not in substring:
                substring += char
                all_possible_substring.append(substring)
            else:
                repeating_char_index = substring.index(char)
                substring = substring[repeating_char_index+1:] + char

        return max([len(item) for item in all_possible_substring])

print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring('dvdf')) # 3