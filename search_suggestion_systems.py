from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        for idx, _ in enumerate(searchWord):
            temp_result = [item for item in products if searchWord[:idx+1] == item[:idx+1]]
            temp_result.sort()
            result.append(temp_result[:3])
        return result

print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")) # [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad', 'mouse']]
print(Solution().suggestedProducts(["bags","baggage","banner","box","cloths"], "bags")) # [['baggage', 'bags', 'banner'], ['baggage', 'bags', 'banner'], ['baggage', 'bags', 'banner'], ['bags', 'baggage', 'bags'], ['bags', 'baggage', 'bags']]