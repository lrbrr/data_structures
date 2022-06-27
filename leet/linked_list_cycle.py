from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    def __repr__(self) -> str:
        return f'{self.val} -> {self.next}'

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False

        current = head
        while current.next:
            if current.val == None:
                return True
            current.val = None
            current = current.next
        return False

example = ListNode(1)
print(Solution().hasCycle(example)) # False

this = ListNode(1)
that = ListNode(2)
this_that = ListNode(3)
this.next = that
that.next = this_that
this_that.next = that
print(Solution().hasCycle(this)) # True