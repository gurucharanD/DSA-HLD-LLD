# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        prev = None
        vio = []
        def inOrder(node):
            nonlocal prev
            if node is None:
                return
            
            inOrder(node.left)
            if prev:
                if prev.val > node.val:
                    if len(vio) == 0:
                        vio.append(prev)
                        vio.append(node)
                    else:
                        vio.pop()
                        vio.append(node)
                        
            prev = node
            inOrder(node.right)
        inOrder(root)
            
        print(vio)
        node1 = vio[0]
        node2 = vio[1]
        node1.val,node2.val = node2.val,node1.val
        
        return root
        
                    
                    