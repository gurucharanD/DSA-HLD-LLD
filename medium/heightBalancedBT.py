# traverse through all the nodes in the tree and 
# check if all the nodes  have both their left and right subtrees
# as height balanced. We need to return the height of the left and right 
# subtrees and check if the difference between them is less than or equal to 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        def isValid(node):
            if node is None:
                return 0
            
            left = isValid(node.left)
            if left == -1:
                return -1
            right = isValid(node.right)
            if right == -1: 
                return -1
            
            if abs(left-right) > 1 : return -1
            
            return 1+max(left,right)
        
        return isValid(root) != -1


