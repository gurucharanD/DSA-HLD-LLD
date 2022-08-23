# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# the width of the binary tree is the max no of Nodes possible 
# between the first and last node of the tree
# assign an index to each node in the binary tree
# if root index = 0
# index of left child node = 2i+1
# index of right child node = 2i+2

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        q = [[root,1]]
        levelOrder = []
        while len(q):
            level = []
            length = len(q)
            for _ in range(length):
                node,rank = q.pop(0)
                if node :
                    level.append(rank)
                    if node.left:
                        q.append([node.left,2*rank])
                    if node.right:
                        q.append([node.right,2*rank+1])
            levelOrder.append(level[:])
        
        maxI = 1
        for level in levelOrder:
            if len(level) > 1:
                mini = level[0]
                maxi = level[-1]
                
                maxI = max(maxI,maxi-mini+1)
                        
        return maxI
            
                    

                    
                
                    

            
            
        
        