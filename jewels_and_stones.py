class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

print(Solution().numJewelsInStones('z', 'ZZ')) # 0
print(Solution().numJewelsInStones('aA', 'aAAbbbb')) # 3