# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    
    def dfs(node,path,target):
        if node is None:
            return False
        
        if node.val == target:
            path.append(node)
            return True
        
        left = False
        if node.left:
            left = dfs(node.left,path,target)
        
        right = False
        if node.right:
            right = dfs(node.right,path,target)
            
        
        if left or right:
            path.append(node)
            
        return left or right        
    
        pathToP = []
        dfs(root,pathToP,p.val)
        pathToP = pathToP[::-1]
        
        return pathToP