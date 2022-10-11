# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
	headOfSum = LinkedList(None)
	print(headOfSum.next)
	carry = 0
	prev = headOfSum
	while linkedListOne is not None or linkedListTwo is not None or carry!=0:
		valueOne = linkedListOne.value if linkedListOne is not None else 0
		valueTwo = linkedListTwo.value if linkedListTwo is not None else 0
		
		currentSum = valueOne + valueTwo + carry
		nodeValue = currentSum % 10
		carry = currentSum // 10
		
		if headOfSum.value is None:
			headOfSum.value = nodeValue
		else:
			node = LinkedList(nodeValue)
			prev.next = node
			prev = node
			
		linkedListOne = linkedListOne.next if linkedListOne is not None else None
		linkedListTwo = linkedListTwo.next if linkedListTwo is not None else None
		
		
		
		
		
    return headOfSum
