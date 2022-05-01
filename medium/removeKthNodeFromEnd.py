# This is an input class. Do not edit.
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
