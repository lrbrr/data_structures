from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f'{self.val} -> {self.next}'

class Solution:
    def create_num(self, linkl: Optional[ListNode]):
        out = []
        while linkl.next:
            out.append(linkl.val)
            linkl = linkl.next
        out.append(linkl.val)
        return int("".join([str(i) for i in out][::-1]))
        
    def create_ll(self, num_list: List[int]) -> Optional[ListNode]:
        if len(num_list) == 1:
            return ListNode(num_list[0])
        return ListNode(num_list[0], self.create_ll(num_list[1:]))
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.create_num(l1)
        num2 = self.create_num(l2)
        
        result = num1 + num2
        
        reversed_list = [int(i) for i in str(result)[::-1]]

        return self.create_ll(reversed_list)

print(Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))
print(Solution().addTwoNumbers(ListNode(0), ListNode(0)))