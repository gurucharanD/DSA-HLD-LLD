# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedDict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        right_view = SortedDict()
        left_view =  SortedDict()
        
        def right_view_traversal(node,level):
            if not node:
                return
            
            right_view[level] = node.val
            right_view_traversal(node.left,level+1)
            right_view_traversal(node.right,level+1)

            
        right_view_traversal(root,0)
        print('right',right_view.values())
        
        def left_view_traversal(node,level):
            if node is None:
                return
            
            if level not in left_view:
                left_view[level] = node.val
            
            left_view_traversal(node.left,level+1)
            left_view_traversal(node.right,level+1)
        
        left_view_traversal(root,0)
        print('left',left_view.values())
            