# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(logN)^2 as we are only visiting logN nodes 
# for logN height

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if node is None:
                return 0
            
            left = getleftHeight(node.left)
            right = getRightHeight(node.right)
            
            if left == right:
                return (2 << left )-1
            
            return 1+helper(node.left)+helper(node.right)
        
        def getleftHeight(node):
            count = 0
            while node is not None:
                count+=1
                node = node.left
            
            return count
        
        def getRightHeight(node):
            count = 0
            while node is not None:
                count+=1
                node = node.right
            
            return count
        
        return helper(root)
        