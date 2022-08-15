# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p1 = head
        p2 = head
        cycle = False
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                cycle = True
                break
        
        if not cycle:
            return None
        
        p1 = head
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
        (self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p1 = head
        p2 = head
        cycle = False
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                cycle = True
                break
        
        if not cycle:
            return None
        
        p1 = head
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
        