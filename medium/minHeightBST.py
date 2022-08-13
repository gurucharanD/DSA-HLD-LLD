def minHeightBst(array):
	return constructBST(array,None,0,len(array)-1)

def constructBST(array,bst,left,right):
	if left > right:
		return
	mid = (left+right)//2
	element_to_insert = array[mid];
	
	if bst is None:
		bst = BST(element_to_insert);
	else:
		bst.insert(element_to_insert);
		
	constructBST(array,bst,left,mid-1)
	constructBST(array,bst,mid+1,right)
	
	return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)



# since the array is sorted
# to have a BST that is balanced in height
# we should try to build a balanced tree with
# equal number of nodes in right and left sub trees

# so the middle element needs to be the root of the Tree
# and we recursively invoke the function on the left and right 
# sub arrays 

# if the BST is empty we create a new BST, 
# else we add the Element at the middle of the array 
# into the BST
