p# This is an input class. Do not edit.
from opcode import HAVE_ARGUMENT
from platform import node
from time import thread_time
from matplotlib.pyplot import thetagrids
from numpy import Infinity, greater, maximum, minimum
from pandas import value_counts


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
	return validator(tree,float("-inf"),float("inf"))

def validator(node,minValue,maxValue):
	
	if node is None:
		return True;
	
	if node.value < minValue or node.value >= maxValue:
		return False;
	
	return validator(node.left,minValue,node.value) and validator(node.right,node.value,maxValue)
	

# Every node in BST has a minimum value and maximum value
# that depends on the position of the node

# the value of a right node has to be greater than or equal to 
# the value of its root hence the minimum value of the right node is going to 
# always stricily less than or eqaul to its parent value
# the maximum value comes from the maximum value its parent can have


# the value of left node is always going to be less than the 
# value of the root node, hence the maximum value a left node
# is going to have is the value of its parent strictly
# the minimum value comes from the minimum value its parent can have



        #       10
        #     /     \
        #    5      15
        #   / \    /  \
        #  2   5  13   22
        # /        \
        # 1         14  


# consider node 2 => the maximum value node 2 can have is less than 5 and 
# the minimum value it can have is -Infinity as it is the minimum value that
# its parent 

# consider node 22 => the minimum value it can have is 15 and 
# the maximum value it can have is Infinity as it is the maximum value 
# of its parent node

# node 5 at level 3 => the minimum value it can have 5 and the maximum value 
# it can have is less than 10 since it is the maximum value that 
# its parent can have

# node 13 => the minimum value it can have is 10 and the max value it can have is 15