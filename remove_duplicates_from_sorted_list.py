from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f'{self.val} -> {self.next}'

class Solution:
    def create_list(self, head: Optional[ListNode]) -> List:
        out = []
        while head.next:
            out.append(head.val)
            head = head.next
        out.append(head.val)
        return out
    
    def create_ll(self, nums: List) -> Optional[ListNode]:
        head = ListNode(nums[0])
        curr = head
        for i in range(1, len(nums)):
            curr.next = ListNode(nums[i])
            curr = curr.next
        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        sorted_unique_list = sorted(list(set(self.create_list(head))))
        return self.create_ll(sorted_unique_list)

class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

sample = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
print(Solution().deleteDuplicates(sample)) # 1 -> 2 -> 3 -> None

print(' - ' * 30)

print(Solution2().deleteDuplicates(sample)) # 1 -> 2 -> 3 -> None