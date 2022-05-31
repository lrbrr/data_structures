from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]

print(Solution().nextGreatestLetter(["c", "f", "j"], "a")) # "c"
print(Solution().nextGreatestLetter(["c", "f", "j"], "c")) # "f"
print(Solution().nextGreatestLetter(["c", "f", "j"], "d")) # "f"
print(Solution().nextGreatestLetter(["c", "f", "j"], "g")) # "j"
print(Solution().nextGreatestLetter(["c", "f", "j"], "j")) # "c"
print(Solution().nextGreatestLetter(["c", "f", "j"], "k")) # "c"