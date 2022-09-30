# 655. Print Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def height_dfs(node):
            if node is None:
                return 0
            
            left = height_dfs(node.left)
            right = height_dfs(node.right)
            
            return 1+ max(left,right)
        
        height = height_dfs(root)
        rows = height
        cols = pow(2,height)-1
        
        matrix = [[""]*cols for _ in range(rows)]
        
        def dfs(node,pos,row,col):
            if node is None:
                return
            
            if pos == "root":
                newRow = 0
                newCol = (cols-1)//2
            elif pos == "left":
                newRow = row+1
                newCol = col - pow(2,height-row-2)
            elif pos == "right":
                newRow = row+1
                newCol = col + pow(2,height-row-2)
                        
            matrix[newRow][newCol] = str(node.val)
            dfs(node.left,"left",newRow,newCol)
            dfs(node.right,"right",newRow,newCol)
            
            return
        
        dfs(root,"root",0,0)
        
        return matrix
            
            