# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p == root or q == root:
            return root
        
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
        
        pathToQ = []
        dfs(root,pathToQ,q.val)
        pathToQ = pathToQ[::-1]
                
        sol = root
        for i in zip(pathToQ,pathToP):
            if i[0] == i[1]:
                sol = i[0] 
            else:
                break
        
        return sol

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p == root or q == root:
            return root
        
        def dfs(node,p,q):
            if node is None or node == p or node == q :
                return node
                        
            left = dfs(node.left,p,q)

            right = dfs(node.right,p,q)
                
            
            if left and right:
                return node
                
            if left is not None:
                return left
            if right is not None:
                return right
            
            return None
        
        return dfs(root,p,q)
                            
        
            
            
            
           
            
            
            
        