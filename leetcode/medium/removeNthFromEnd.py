# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2 pass approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        count = 0
        curr = head
        
        while curr:
            count+=1
            curr = curr.next
            
        stopNode = count-n
        
        prev = None
        curr = head
        count = 0
        while count < stopNode:
            prev = curr
            curr = curr.next
            count+=1
        
        
        if prev is None:
            return curr.next
        
        prev.next = curr.next
        return head

# 1 pass approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0);
        dummy.next = head;
        pointer1 = dummy
        pointer2 = dummy
        
        count = 0
        while count <= n:
            pointer1 = pointer1.next
            count+=1
        
        
        while pointer1:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        
        pointer2.next = pointer2.next.next
        return dummy.next