# brute force approach
# is to traverse the tree in in-order Traversable
# and add Elements to a list and this traversal by default gives us a 
# sorted list of the Elements in the tree

# after the entire tree is traversed, then return the 
# kth largest Element by just list[list.length - k-1]

# this approach takes O(n) time and O(n) space
# as you traverse all the nodes in the Tree
# and all the values of all the nodes are saved in the list
# (refer js Code for above solution)

# _______solution 2_________
# 

# in in-order traversal we first go to the least nodes in our traversal
# but our problem asks us to find the largest element. so we should instead do
# a reverse in-order traversal starting from the largest element in the tree first
# which is the right most node in the tree and then go to the least 

# the reverse in-order traversal means that we visit the 
# go to right node  -> visit current node -> go to left node

# this traversal gives us the values in the tree sorted in reverse order
# so once we have visited K nodes in reverse inorder traversal then it is 
# the node we are looking for and we can return the value of that node
# to avoid extra space, we need to keep track of the number of nodes we visited
# and the value of visited node

# the time and space for this approach is O(h+k) and O(h)

# h is  height is the tree, sometimes we need to find the largest element of the tree
# h is for going all the way to the end
# and k is the time reaquired to reach the kth larges element from the largest
# element in the tree
# h space is the max no of recursive calls we have on the stack

# ________________
# 

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		
class TreeInfo:
	def __init__(self,numberOfNodesVisited,latestVisitedNodeValue):
		self.numberOfNodesVisited = numberOfNodesVisited;
		self.latestVisitedNodeValue = latestVisitedNodeValue;


def findKthLargestValueInBst(tree, k):
	treeInfo = 	TreeInfo(0,-1);
	reverseInorderTraversal(tree,k,treeInfo);
	return treeInfo.latestVisitedNodeValue;
	
def reverseInorderTraversal(tree,k,treeInfo):
	
	if tree is None :
		return
		
    # traverse right
	reverseInorderTraversal(tree.right,k,treeInfo)	
	
	if treeInfo.numberOfNodesVisited < k:

        # visit operation
		treeInfo.numberOfNodesVisited += 1 
		treeInfo.latestVisitedNodeValue =  tree.value
		
        # traverse left
		reverseInorderTraversal(tree.left,k,treeInfo)








