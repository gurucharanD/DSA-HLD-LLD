# the no of islands in the grpah
# is the total no of connected components

class Solution:
    
    # visited = []
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(i,j,grid,visited):
            
            if i < 0 or j < 0 : return
            if i >= len(grid) or j >= len(grid[0]): return
            if visited[i][j] == 1 or grid[i][j] == "0": return
            
            visited[i][j] = 1

            dfs(i-1,j,grid,visited)
            dfs(i+1,j,grid,visited)
            dfs(i,j-1,grid,visited)
            dfs(i,j+1,grid,visited)

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j] == "1" and visited[i][j] == 0:
                    
                    dfs(i,j,grid,visited)
                    count+=1


        return count



            
            
        