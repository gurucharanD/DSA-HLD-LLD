
# use two pointers that move at different pace
# pointer1 moves at 1 node per step
# pointer2 mpves at 2 nodes per step

# when the two pointers meet, there is a loop

# after the loop is found 
# move one pointer to the head and 
# move the pointers at same speed now

# when the two pointers meet again
# that is where the loop begins



class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
	
	node = head
	pointer1 = head
	pointer2 = head
	
	while pointer2 is not None and pointer2.next is not None:
		pointer1 = pointer1.next
		pointer2 = pointer2.next.next
		
		print(pointer1.value, pointer2.value)
		
		if pointer1 == pointer2:
			# print("loop")
			break
		
	pointer1 = head
	
	while pointer1 != pointer2:
		pointer1 = pointer1.next
		pointer2 = pointer2.next
		
	
	return pointer1
		

		
# Leetcode
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None or head.next is None:
            return False
        
        pointer1 = head.next
        pointer2 = head.next.next
        
        while pointer2 is not None and  pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
            if pointer1 == pointer2:
                return True
        
        return False
    
