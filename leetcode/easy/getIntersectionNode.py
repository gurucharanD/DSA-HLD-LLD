# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# when one pointer reaches the end of the linked list
# move that pointer to the beginning of the other otherlinked list
# in this way we are countering out the differences in the lengths 
# of the linkedlists
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB
        
        while p!=q:
            
            p = p.next if p is not None else headB
            q = q.next if q is not None else headA
        
        return p
        