from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            diff = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit = max(diff, max_profit)
            else:
                left = right
            right += 1
        return max_profit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        
        return max_profit

print(Solution().maxProfit([7,6,4,3,1])) # 0
print(Solution().maxProfit([7,1,5,3,6,4])) # 5
print(Solution().maxProfit([7,2,5,3,1,4])) # 3

print(' - ' * 30)

print(Solution2().maxProfit([7,6,4,3,1])) # 0
print(Solution2().maxProfit([7,1,5,3,6,4])) # 5
print(Solution2().maxProfit([7,2,5,3,1,4])) # 3