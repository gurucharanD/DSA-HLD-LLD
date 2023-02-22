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
# pointer 1 and pointer 2 are pointing to head pointer
# assume the length of the of the linked list is L
# pointer1 will move N steps first
# when there are L-N steps remaining 
# pointer2 will start moving along with pointer1
# they will move simaltaneously
# when pointer1 reaches the end of the list
# pointer 2 will be at the place where the 
# pointer2.next is the node that needs to be removed

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