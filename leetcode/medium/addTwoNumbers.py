# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(-1)
        root = head
        
        p1 = l1
        p2 = l2
        carry = 0
        
        while p1 or p2 or carry:
            add =  ( p1.val if p1 else 0 ) +  ( p2.val if p2 else 0 ) + carry
            
            carry =  add //10
            
            head.next = ListNode(add % 10)
            head = head.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            
        
        return root.next
        
