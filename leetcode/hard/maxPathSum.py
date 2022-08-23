# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.val
        
        maxValue = float("-inf")
        def helper(node):
            nonlocal maxValue
            if node is None:
                return 0
            
            # if a node has a negative path sum
            # consider it as 0
            left = max(0,helper(node.left))
            right = max(0,helper(node.right))
            
            # at every node caluculate the maxvalue of
            # the path sum
            maxValue = max(maxValue,left+right+node.val)
            
            # return the max path at the node
            return node.val+max(left,right)
        
        helper(root)
        return maxValue
        