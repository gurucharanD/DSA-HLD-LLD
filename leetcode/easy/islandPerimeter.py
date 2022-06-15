# when an edge case is reached , return 1
# as it is the border of the land


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(i,j,grid,visited):
            
            if  ( i >= len(grid) or j >= len(grid[0])) or ( i < 0 or j < 0 ) or grid[i][j] == 0 : return 1
            if visited[i][j] == 1: return 0
            
            visited[i][j] = 1
            
            return dfs(i-1,j,grid,visited) + dfs(i+1,j,grid,visited) + dfs(i,j-1,grid,visited) + dfs(i,j+1,grid,visited) 

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    return dfs(i,j,grid,visited)
        
