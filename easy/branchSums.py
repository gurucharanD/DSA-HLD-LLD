# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	result = []
	branchSumHelper(root,result,0)	
	return result

def branchSumHelper(node,result,sum):
	sum += node.value
	if node.right is None and node.left is None:
		return result.append(sum)
	
	if node.left is not None:
		branchSumHelper(node.left,result,sum)
		
	if node.right is not None:
		branchSumHelper(node.right,result,sum)


# start at the starting node of the tree i.e root
# and keep moving to the left childs of the tree first until you reach the end
# at ecach node keep caluclating the sum of the nodes that are visited
# once you reach the end push the sum thus far into the array and return

# base case is when you reach the end of the tree and have no more children
# recursively call the same function on both left and right childs

# here we are passing the reference of the result array into the function
# so after the function ends, the result will have the actual result of the problem
