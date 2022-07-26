# 86. Partition List
# create 2 seperate linked lists 
# that keep track of the 
# smaller elements than x in the list and
# elements greater than x in the list
# and merge them at the end

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        small = ListNode(-1)
        large = ListNode(-1)
        
        smallHead = small
        largeHead = large
        
        while head:
            
            if head.val < x:
                small.next = head
                head = head.next
                small = small.next
                small.next = None
            
            else:
                large.next = head
                head = head.next
                large = large.next
                large.next = None
            
        small.next = largeHead.next
        return smallHead.next
                
        