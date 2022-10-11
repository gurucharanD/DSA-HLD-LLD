# This is an input class. Do not edit.
# place 2 pointers p1 and p2 at the head of LL
# move p2 by k steps first
# then move both pointers p1 and p2 together unitl one of them reaches end
# when one of them reaches the end
# the node pointed by p1 is the node to be removed
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	counter = 1
	pointer1 = head
	pointer2 = head
	
	while counter != k:
		pointer2 = pointer2.next
		counter+=1
		
	if pointer2.next == None:
		head.value = head.next.value
		head.next = head.next.next
		return head
	
	prev = None
	while pointer1.next is not None and pointer2.next is not None:
		prev = pointer1
		pointer1 = pointer1.next
		pointer2 = pointer2.next
			
	prev.next = pointer1.next
	
	return head
