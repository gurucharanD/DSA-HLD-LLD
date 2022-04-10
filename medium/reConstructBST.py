
# solution 1: with O(n^2) and O(h) space

# since the array we are given has a pre-order traversal of the elements
# the first element of the array is the root of the tree
# then we traverse through the array to find the root of the right sub tree
# the root of the right subtree is the element after the root that is greater than
# or equal to the root element. 

# once the root is found we break the array into two halfs and build the left and right
# sub trees recursively and return the BST(value,leftTree,rightTree)

# this solution has a run time complexity of O(n^2) as at every node 
# we are looping through the array to find the root of right sub tree 
# and this iteration takes O(n) and we do this iteration for each element in the 
# array therefore we get O(n^2)

# the space complexity for this approach is O(h) as at any point
# we will h calls on our call stack as we keep goinf to the left left until the 
# last child node is reached


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
	
	if len(preOrderTraversalValues)==0:
		return
	
	root = preOrderTraversalValues[0];
	rightIndex = len(preOrderTraversalValues);
	
	for i in range(1,len(preOrderTraversalValues)):
		if preOrderTraversalValues[i] >= root:
			rightIndex = i
			break
			
	print(rightIndex)
	
	leftTree = reconstructBst( preOrderTraversalValues[1:rightIndex] )
	rightTree = reconstructBst( preOrderTraversalValues[rightIndex:] )
	
	return BST(root,leftTree,rightTree);

			

# solution 2: O(n) time and space

# instead of looping through the array mulitple times
# we trave through the array only once and at each element we 
# keep track of the min and max value the node can take 
# min and max value are derived from validate BST problem
# at every point we keep track of the index, 
# once the index reaches the length of the array we return

		
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		
class TreeInfo:
	def __init__(self,rootIdx):
		self.rootIdx = rootIdx


def reconstructBst(preOrderTraversalValues):
	treeInfo = TreeInfo(0)
	return reconstructBstWithRange(preOrderTraversalValues,float("-inf"),float("inf"),treeInfo)

def reconstructBstWithRange(preOrderTraversalValues,minValue,maxValue,treeInfo):
	if treeInfo.rootIdx == len(preOrderTraversalValues):
		return
	
	rootValue = preOrderTraversalValues[treeInfo.rootIdx]
	
	if minValue > rootValue or rootValue >= maxValue:
		return
	
	treeInfo.rootIdx+=1
	
	leftTree = reconstructBstWithRange(preOrderTraversalValues,minValue,rootValue,treeInfo)
	rightTree = reconstructBstWithRange(preOrderTraversalValues,rootValue,maxValue,treeInfo)
	
	return BST(rootValue,leftTree,rightTree)

	

	
