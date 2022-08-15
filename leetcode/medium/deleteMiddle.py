# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer1 = head
        pointer2 = head
        prev = None
        while pointer2 and pointer2.next:
            prev = pointer1
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
        
        if prev is None:
            return pointer1.next
        
        prev.next = pointer1.next
        return head
        