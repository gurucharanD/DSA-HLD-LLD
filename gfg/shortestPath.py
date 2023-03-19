#User function Template for python3
# Shortest path in Undirected Graph having unit distance


from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adjList = [[] for _ in range(n)]
        for s,d in edges:
            adjList[s].append(d)
            adjList[d].append(s)
        
        q = deque([src])
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        
        while q:
            node = q.popleft()
            for nei in adjList[node]:
                if dist[nei] > dist[node]+1:
                    dist[nei] = dist[node]+1
                    q.append(nei)
        
        for idx,val in enumerate(dist):
            if dist[idx] == float("inf"):
                dist[idx]=-1
        
        return dist

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends