# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# find the parent nodes of each node
# we do this so that we can go to the opposite tree of the current node
# starting at the target node, identify do a dfs
# keep track of the visited nodes and find the nodes at distance K
# from the target node  

# this can also be solved using a bfs
# starting at the target node 
# keep track of the node and the distance of
# the node from the target node in a tuple 


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node,parent):
            if node is None:
                return
            
            node.parent = parent
            dfs(node.left,node)
            dfs(node.right,node)
                        
        dfs(root,None)
        
        sol = []
        seen = {}
        
        def dfs(node,seen,distance):
            if distance == k:
                sol.append(node.val)
            
            if distance > k:
                return
            
            seen[node.val] = True
            if node.left and node.left.val not in seen:
                dfs(node.left,seen,distance+1)
            if node.right and node.right.val not in seen:
                dfs(node.right,seen,distance+1)
            if node.parent and node.parent.val not in seen:
                dfs(node.parent,seen,distance+1)
            
            return
        
        dfs(target,seen,0)
        return sol
                
                
            
            
        