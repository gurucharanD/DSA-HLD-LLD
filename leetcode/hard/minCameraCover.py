# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1  = covered
# 0 = montiored
# -1 = need camera

class Solution:
    
    count = 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == -1 or right == -1:
                self.count+=1
                return 1
            
            if left == 1 or right == 1:
                return 0
            
            return -1
            
        
        if dfs(root) == -1:
            return self.count+1
        
        return self.count
        