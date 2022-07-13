
# using the idea that
# all the elements int the Q before the iteration begins
# belong to the same level

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        sol = []
        q = [root]
        
        while len(q):
            level = []
            length = len(q)
            for _ in range(length):
                node = q.pop(0)
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
            sol.append(level[:])
            
        return sol
        
        