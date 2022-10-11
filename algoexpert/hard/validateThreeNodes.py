# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
	return finder(nodeOne,nodeThree,nodeTwo) or  finder(nodeThree,nodeOne,nodeTwo)
			
def finder(source,tagrget,middle):
	node = source
	nodeTwoFound = False
	while node is not None:
		if node.value == tagrget.value:
			if nodeTwoFound:
				return True
			else:
				return False
		if node.value == middle.value:
			nodeTwoFound = True
			
		if tagrget.value < node.value:
			node = node.left
		else:
			node = node.right
	
    return False
