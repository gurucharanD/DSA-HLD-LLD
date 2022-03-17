
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	# Write your code here.
	currentNode = linkedList;
	while currentNode.next is not None:
		nextNode = currentNode.next
		if currentNode.value == nextNode.value:
			currentNode.next = nextNode.next
		else:
			currentNode = nextNode
			
			
	return linkedList
