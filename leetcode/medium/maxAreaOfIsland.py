# find the connected components 
# and find the connected component with max
# count of nodes
# the base cases return 0
# at the end of recursively invoking the neighbours
# return 1 plus the values returned by the neighbours

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        count = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            
        def dfs(i,j,grid,visited):
            
            if i < 0 or j < 0: return 0
            if i >= len(grid) or j >= len(grid[0]): return 0
            if grid[i][j] == 0 or visited[i][j] == 1: return 0
            
            visited[i][j] = 1
            
            top = dfs(i-1,j,grid,visited)
            bottom = dfs(i+1,j,grid,visited)      
            left = dfs(i,j-1,grid,visited)
            right = dfs(i,j+1,grid,visited)

            return 1 + (top+bottom+left+right)
            
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    count = max(count,dfs(i,j,grid,visited))
        
        return count
        