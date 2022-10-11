
# solution 1 : bruteforce solution is to 
# find the inorder traversal of the tree first 
# and then find the Element next to the key in the array

# O(n) time and space as we iterate over each node in the tree 
# and we need to save the traversal order in an array

# solution 2 : 
# the successor of a node in the in-order traversal is the 
# farthest left node in the right sub-tree of that Node
# if the node has a right sub-tree
# else the successor is the right most ancestor

# this allows us to solve the problem in O(h) time
# which is O(logn) logn is the height of the tree
# O(1) space as we only keep track of the left or right node
# or the ancestor


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
	if node.right is not None:
		return getLeftMostChild(node)
    return getRightMostParent(node)

def getLeftMostChild(node):
	currentNode = node.right
	
	while currentNode.left is not None:
		currentNode = currentNode.left
	return currentNode

def getRightMostParent(node):
	currentNode = node
	while currentNode.parent is not None and currentNode.parent.right == currentNode:
		currentNode = currentNode.parent
		
	return currentNode.parent


