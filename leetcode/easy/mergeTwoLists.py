# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if list1 is None:
            print("list1 is None")
            return list2
        
        if list2 is None:
            print("list2 is None")
            return list1
        
        p1 = list1
        p2 = list2
        
        
        output = ListNode(-1)
        head = output
        
        while p1 and p2 :
            
            if p1.val <= p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2
                p2 = p2.next
            
            head = head.next
            
        while p1 :
            head.next = p1
            p1 = p1.next
            head = head.next

        while p2:

            head.next = p2
            p2 = p2.next
            head = head.next

            
        return output.next