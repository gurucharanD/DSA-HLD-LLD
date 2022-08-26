'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    # Write your code here.
    
    ceil = -1
    while root is not None:
        if root.data == x:
            return root.data
        
        if x > root.data:
            root = root.right
        else:
            ceil = root.data
            root = root.left
     
    return ceil
            