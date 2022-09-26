# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        visited = set()
        
        while curr:
            if curr.val in visited:
                prev.next = curr.next
                curr = curr.next
            else:
                visited.add(curr.val)
                prev = curr
                curr = curr.next
                
                
        
        return head