# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = [root]
        ans = []
        zigzag = False
        while q:
            
            length = len(q)
            level = [0]*length
            for i in range(length):
                node = q.pop(0)
                if node:
                    index = length-i-1 if zigzag else i
                    level[index] = node.val
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            

            ans.append(level)
            zigzag = not zigzag
        
        return ans
                
                
                
        