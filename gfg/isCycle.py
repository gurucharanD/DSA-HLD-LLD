# cycle in undirected graph
# if the dfs is making you to visit a neighbour that is already visited
# except for the parent node that was used to reach the current node
# then we can conform that there is a cycle in the graph

# the similar technique holds true for BFS traversal as well
# by keeping track of the parent node

# dfs approach
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		def dfs(node,par):
		    if node in visited:
		        return False
		        
		    visited.add(node)
		    
		    res = False
		    for nei in adj[node]:
		        if nei in visited:
		            if nei == par:
		                continue
		            else:
		                return True
		        else:
		            res = res or dfs(nei,node)
		    return res
		    
		visited = set()
		for node,lis in enumerate(adj):
		    if node not in visited:
                if dfs(node,None):
                    return True
		
		return False
		   
#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends

# bfs approach

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
	    
	    def bfs(node):
	        q = [(node,-1)]
	        
	        while q:
	            curr,par = q.pop(0)
	            visited.add(curr)
	            for nei in adj[curr]:
	                if nei in visited:
	                    if nei == par:
	                        continue
	                    else:
	                        return True
	                else:
	                    q.append((nei,curr))
	                    
	        return False
	        
	    visited = set()
	    for node,lis in enumerate(adj):
	        if node not in visited:
    	        if bfs(node):
    	            return True
	   
	    return False
	                    
	        
#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends