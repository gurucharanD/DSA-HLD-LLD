# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	depthOfOne = findDepthOfAncestor(descendantOne)
	depthOfTwo = findDepthOfAncestor(descendantTwo)
	
	differenceInDepth = abs(depthOfOne - depthOfTwo)
	
	if depthOfOne > depthOfTwo:
		descendantOne = balanceNode(descendantOne,differenceInDepth)
	elif depthOfTwo > depthOfOne:
		descendantTwo = balanceNode(descendantTwo,differenceInDepth)
	
	print(descendantOne.name,descendantTwo.name)
	
	if descendantOne.name == descendantTwo.name:
		return descendantOne
	
	# if descendantOne.ancestor.name == descendantTwo.ancestor.name:
	# 	return descendantOne.ancestor
	
	while descendantOne.ancestor is not None and descendantTwo.ancestor is not None:
		
		if descendantOne.ancestor.name == descendantTwo.ancestor.name:
			return descendantOne.ancestor
		
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor

def balanceNode(node,depth):
	while depth > 0:
		node = node.ancestor
		depth-=1
	return node

def findDepthOfAncestor(node):
	depth = 0
	while node.ancestor is not None:
		depth+=1
		node = node.ancestor
	
	return depth