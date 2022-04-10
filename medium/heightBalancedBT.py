# traverse through all the nodes in the tree and 
# check if all the nodes  have both their left and right subtrees
# as height balanced. We need to return the height of the left and right 
# subtrees and check if the difference between them is less than or equal to 1


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		
class TreeInfo:
	def __init__(self,isValid,height):
		self.isValid = isValid
		self.height = height


def heightBalancedBinaryTree(tree):
	treeInfo = getTreeInfo(tree)
	return treeInfo.isValid;
	
def getTreeInfo(tree):
	
	if tree is None:
		return TreeInfo(True,0)
	
	leftTree = getTreeInfo(tree.left)
	rightTree = getTreeInfo(tree.right)
	
	isValid = (leftTree.isValid and rightTree.isValid and abs(rightTree.height - leftTree.height) <= 1)
	height = max(leftTree.height,rightTree.height) + 1
	
	return TreeInfo(isValid,height)
	 



