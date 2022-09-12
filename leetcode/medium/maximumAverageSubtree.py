# for any problem involving the average in a binary tree
# return the no of nodes involved and the sum of the nodes involved

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        ans = float("-inf")
        def dfs(node):
            nonlocal ans
            if node is None:
                return (0,0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            numOfElems = 1 + left[0]+right[0]
            sumOfElems = node.val + left[1] + right[1]
            
            ans = max(ans,sumOfElems/numOfElems)
            
            return (numOfElems,sumOfElems)
        
        
        dfs(root)
        return ans