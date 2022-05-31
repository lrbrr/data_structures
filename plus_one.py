from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits))) + 1
        result = list(map(int, ([i for i in str(number)])))
        return result
    
print(Solution().plusOne([9])) # [1, 0] 
print(Solution().plusOne([1,2,3])) # [1, 2, 4]
print(Solution().plusOne([4,3,2,1])) # [4, 3, 2, 2]