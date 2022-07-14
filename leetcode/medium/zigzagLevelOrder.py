# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        q = [root]
        levelOrder = []
        swap = True
        
        while len(q):
            level = []            
            for _ in range(len(q)):
                node = q.pop(0)
                if node is not None:
                    level.append(node.val)
                     
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
                        
            if swap == True:
                levelOrder.append(level)
            else:
                levelOrder.append(level[::-1])
            
            swap = not swap

                
        return levelOrder
            
                           
        