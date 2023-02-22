# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [root]
        preOrder = []
        
        while stack:
            
            currNode = stack.pop()
            if currNode:
                preOrder.append(currNode.val)
                # append the right node first because
                # in a stack, the last element inserted
                # will be popped out first
                if currNode.right:
                    stack.append(currNode.right)
                if currNode.left:
                    stack.append(currNode.left)
                
            
        return preOrder    
        