# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levelOrder = {}
        q = [[root,0]]
        
        # def bfs(node,level):
        while len(q):
            
            node,level = q.pop(0)
            if node:
                if level in levelOrder:
                    levelOrder[level].append(node.val)
                else:
                    levelOrder[level] =  [ node.val ]

                q.append([node.left,level+1])
                q.append([node.right,level+1])
            
        
        print(levelOrder)
        ans = []
        for level in levelOrder:
            ans.append(levelOrder[level][-1])
        
        return ans


            
            