def findClosestValueInBst(tree, target):
    # Write your code here.
	nearestValue = tree.value
	while tree is not None:
		distance = abs(tree.value - target)
		distanceFromNearest = abs(nearestValue - target)
		
		if(distance<distanceFromNearest):
			nearestValue = tree.value
		
		if target < tree.value:
			tree = tree.left
		else:
			tree = tree.right

			
    return nearestValue


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Assume nearest value for the target is the root
# and start traversing the tree from root
# 
# compare the nearest value that you know, with the node
# that you are visiting, 
# if distance from current node is less than current node we are at,
# update the nearest value with current node
# if the target is less than current node value then go to the left of the tree. 
# as the values that are closest to the target lie in the left half of the tree
# else go to right 

# and keep traversing the tree until all the nodes are traversed