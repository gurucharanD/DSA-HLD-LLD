# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        stack = [[root,1]]
        preOrder = []
        postOrder = []
        inOrder = []
        
        while len(stack):
            node = stack.pop()
            
            if node[1] == 1:
                preOrder.append(node[0].val)
                node[1]+=1
                stack.append(node)
                
                if node[0].left :
                    stack.append([node[0].left,1])
            elif node[1] == 2:
                inOrder.append(node[0].val)
                node[1]+=1
                stack.append(node)
                
                if node[0].right :
                    stack.append([node[0].right,1])
            else:
                postOrder.append(node[0].val)
                
        
        print(inOrder)
        print(preOrder)
        print(postOrder)
        
        return inOrder
        
        

                
            
            
        
        