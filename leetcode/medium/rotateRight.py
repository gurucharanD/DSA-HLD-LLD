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
        

        # move pointer1 to the node
        # which becomes the head after 
        # list is rotated k times
        count = 0
        while count < k and pointer1:
            pointer1 = pointer1.next if pointer1.next else head
            count+=1
            
        # move pointer1 to tail and
        # move pointer2 to the new head
        while pointer1 and pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        # join tail to head
        pointer1.next = head
        # make new node as head
        head = pointer2.next
        # break the link to new head
        # from its previous node
        pointer2.next = None
        
        
        return head
        
        