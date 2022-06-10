class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:        
        end_pos = len(s)-1
        char_count = 0
        
        while s[end_pos] == ' ':
            end_pos -= 1
            
        while s[end_pos] != ' ' and end_pos >= 0:
                char_count += 1
                end_pos -= 1
        return char_count
        
print(Solution().lengthOfLastWord("Hello World")) # 5
print(Solution().lengthOfLastWord("a")) # 1
print(Solution().lengthOfLastWord("   fly me   to   the moon  ")) # 4

print(' - ' * 50)

print(Solution2().lengthOfLastWord("Hello World")) # 5
print(Solution2().lengthOfLastWord("a")) # 1
print(Solution2().lengthOfLastWord("   fly me   to   the moon  ")) # 4