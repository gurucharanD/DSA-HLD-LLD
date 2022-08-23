# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# go to the rightmost node
attach its left 
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        prev = None
        def helper(node):
            nonlocal prev
            if node is None:
                return
            
            helper(node.right)
            helper(node.left)
            
            node.left = None
            node.right = prev
            prev = node
            
        return helper(root)
        