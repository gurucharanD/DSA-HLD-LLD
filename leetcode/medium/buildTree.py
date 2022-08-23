# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre,ino):
            
            if ino:
                val = pre.pop(0)
                currNode = TreeNode(val)
                
                index = ino.index(val)
                
                currNode.left = helper(pre,ino[:index])
                currNode.right = helper(pre,ino[index+1:])
                
                return currNode
        
        return helper(preorder,inorder)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        
        def helper(ino,pos):
            
            if ino and pos:
                val = pos.pop() 
                currNode = TreeNode(val)
                
                index = ino.index(val)
                
                currNode.right = helper(ino[index+1:],pos)
                currNode.left = helper(ino[:index],pos)
                
                return currNode
        
        return helper(inorder,postorder)
                

            
            
                      

            
            
        