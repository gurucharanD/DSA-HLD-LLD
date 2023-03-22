# Shortest Path in Weighted undirected graph
# use dijkstras algo to find the shortest distance
# between the source node and every other node
# every time a shortest distance to a node is found
# track the parent of this node and save it in an
# array called as parent
# once the distances are calculated.. 
# backtrack from destination node to parent node
# to find the path

from collections import deque
class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        adjList = [[] for _ in range(n+1)]
        for s,d,w in edges:
            adjList[s].append((d,w))
            adjList[d].append((s,w))
        
        q = deque([1])
        dist = [float("inf") for _ in range(n+1)]
        parent = [-1 for _ in range(n+1)]
        
        dist[1] = 0
        
        while q:
            node = q.popleft()
            for nei,wei in adjList[node]:
                if dist[nei] > dist[node]+wei:
                    dist[nei] = dist[node]+wei
                    parent[nei] = node
                    q.append(nei)

        if dist[n] == float("inf"):
            return [-1]
        else:
            ans = []
            node = n
            while node!=-1:
                ans.append(node)
                node = parent[node]
            
            return ans[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends