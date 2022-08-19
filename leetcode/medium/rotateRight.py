# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 61. Rotate List

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return head
        
        noOfNodes = 0
        curr = head
        while curr:
            curr = curr.next
            noOfNodes+=1
        
        k = k % noOfNodes
        pointer1 = head
        pointer2 = head
        
        count = 0
        while count < k and pointer1:
            pointer1 = pointer1.next if pointer1.next else head
            count+=1
            
        while pointer1 and pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        
        pointer1.next = head
        head = pointer2.next
        pointer2.next = None
        
        
        return head
        
        