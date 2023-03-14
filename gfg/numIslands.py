#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        #code here
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if (i,j) in visited:
                return
            if grid[i][j] == 0:
                return
            
            visited.add((i,j))
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j+1)
            dfs(i-1,j-1)
            dfs(i-1,j+1)
            dfs(i+1,j-1)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends