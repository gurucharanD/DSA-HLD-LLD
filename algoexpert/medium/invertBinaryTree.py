# iterative approach: O(n) Time, n is the no of nodes and we are exploring every node
# O(n) space, we are using the stack

# Traverse the tree using the BFS using a Queue
# push the root of the tree into the Q first and 
# start iterating over the Q until it is empty

# for each node that you iterate swap the left and
# right subtrees and push the left and right subtrees
# into the Queue

def invertBinaryTree(tree):
	queue = [tree]
	
	while len(queue)!= 0:
		currentNode = queue.pop(0);
		
		if currentNode is None:
			continue
		
		temp = currentNode.left;
		currentNode.left = currentNode.right;
		currentNode.right = temp;
		
		queue.append(currentNode.left);
		queue.append(currentNode.right);

    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




# recursive apporach: is better in terms of space which is O(D)
# where D is the depth of the tree, which is equal to logN
# therefore, space = O(logN)
# the longest recursive call we can ever make is the depth of the tree
# but still has the same time

def invertBinaryTree(tree):
    # Write your code here.
	if tree is None:
		return
	
	temp = tree.left;
	tree.left = tree.right;
	tree.right = temp;
	
	if tree.left is not None:
		invertBinaryTree(tree.left)
		
	if tree.right is not None:
		invertBinaryTree(tree.right)

	
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


