class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opened_braces = ['(', '{', '[']
        closed_braces = [')', '}', ']']
        
        for char in s:
            if char in opened_braces:
                stack.append(char)
                continue

            if char in closed_braces and len(stack) == 0:
                return False
            else:
                popped_brace = stack.pop(-1)
                if opened_braces.index(popped_brace) != closed_braces.index(char):
                    return False

        if len(stack):
            return False
        else:
            return True

class Solution2:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()","").replace("{}","").replace("[]","")
        return len(s) == 0

print(Solution().isValid("()")) # True
print(Solution().isValid("()[]{}")) # True
print(Solution().isValid("(]")) # False
print(Solution().isValid("([)]")) # False
print(Solution().isValid("{[]}")) # True
print(Solution().isValid("{[()]}")) # True
print(Solution().isValid("((")) # False
print(Solution().isValid("]")) # False

print(' - ' * 50)

print(Solution2().isValid("()")) # True
print(Solution2().isValid("()[]{}")) # True
print(Solution2().isValid("(]")) # False
print(Solution2().isValid("([)]")) # False
print(Solution2().isValid("{[]}")) # True
print(Solution2().isValid("{[()]}")) # True
print(Solution2().isValid("((")) # False
print(Solution2().isValid("]")) # False