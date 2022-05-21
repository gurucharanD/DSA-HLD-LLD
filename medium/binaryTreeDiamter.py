
# the diamater of a binary tree is 
# the longest path in the binary Tree that may or may not
# go through the root

# perform a depth first search traversal of the tree
# and at each point calculate the maximum height and diameter 

# the way we consider the diameter is we consider the 
# diameter of the left sub-tree and right sub-tree and 
# then we find the sum of both 


# at every node we do: 
# first we recursively invoke the function on both left and right sub-trees

# then find the longestPossiblePath through that node, 
# which is the sum of heights of left and right sub-trees

# and then find the max Diamter of the left and right sub trees
# which becomes the maxDiameter

# then we find the max of the longestPossiblePath and maxDiameter
# which becomes our currentDiameter

# then we find the currentHeight which is 1 + max of height of left and right sub-trees

# O(n) time

# This is an input class. Do not edit.

# the longest diameter may be passing through the root and may also pass through the children
# that is why we find the max diameter passing through root 
# and max diamater among children
# and the max of these two becomes the max diameter thus far

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self,height,diameter):
		self.height = height
		self.diameter = diameter

def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter;

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0)
	
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
	
	maxDiameterSoFar = max(leftTreeInfo.diameter,rightTreeInfo.diameter)
	
	currentDiameter = max(maxDiameterSoFar,longestPathThroughRoot)
	currentHeight = 1+max(leftTreeInfo.height , rightTreeInfo.height)
	
	return TreeInfo(currentHeight,currentDiameter)

	
	