at every node check two things
if the sum of the root and
the children is max or just the branch is max 
return the maximim value to the previous 


O(n) time and O(logN) space
as at every step we have only logN recursive calls on the stack



def maxPathSum(tree):
	_, maxSum = findMaxSum(tree)
	return maxSum

def findMaxSum(tree):
	if tree is None:
		return (0,float("-inf"))
	
	leftMaxSumAsBranch,leftMaxPathSum = findMaxSum(tree.left)
	rightMaxSumAsBranch,rightMaxPathSum = findMaxSum(tree.right)
	maxChildAsBranch = max(leftMaxSumAsBranch,rightMaxSumAsBranch)
	
	value = tree.value
	maxSumAsBranch = max(maxChildAsBranch+value,value)
	maxSumAsRootNode = max(leftMaxSumAsBranch+value+rightMaxSumAsBranch,maxSumAsBranch)
	maxPathSum = max(leftMaxPathSum,rightMaxPathSum,maxSumAsRootNode)
	
	return (maxSumAsBranch,maxPathSum)