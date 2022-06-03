from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f'{self.val} -> {self.next}'

class Solution:
    def create_list(self, ll: Optional[ListNode]) -> List[int]:
        result = []
        while ll.next:
            result.append(ll.val)
            ll = ll.next
        result.append(ll.val)
        return result

    def create_ll(self, nums: List[int]) -> Optional[ListNode]:
        head = pos = ListNode(nums[0])
        for i in nums[1:]:
            pos.next = ListNode(i)
            pos = pos.next
        return head        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        nums1 = self.create_list(list1)
        nums2 = self.create_list(list2)
        nums = sorted(nums1 + nums2)

        return self.create_ll(nums)

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
print(Solution().mergeTwoLists(list1, list2)) # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

list1 = ListNode(0)
list2 = ListNode(0)
print(Solution().mergeTwoLists(list1, list2)) # 0 -> None