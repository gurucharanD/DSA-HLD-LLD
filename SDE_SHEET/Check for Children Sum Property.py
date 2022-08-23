'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
        
def changeTree(root): 
    # Write your code here.
    def helper(node):
        if node is None:
            return
        
        left = node.left.data if node.left else 0
        right = node.right.data if node.right else 0
        
        total = left + right
        if total > node.data:
            node.data = total
        elif total < node.data:
            if node.left:
                node.left.data = total
            if node.right:
                node.right.data = total
       
        helper(node.left)
        helper(node.right)
        
        left = node.left.data if node.left else 0
        right = node.right.data if node.right else 0
        
        total = left+right
        if node.left or node.right:
            node.data = total
    helper(root)
    return root
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    pass