# the top row and left most column is touching pacific ocean
# the bottom row and right most column is touching atlantic ocean

# start from these positions and check which other positions 
# can reach these oceans,and create a set of all the positons
# at the end the intersection of two sets is the required solution
# these are the positions that can meet both the oceans 


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = set()
        atl = set()
        
        rows = len(heights)
        cols = len(heights[0])
        solution = []
        def dfs(i,j,visited,prevHeight):
            
            if i < 0 or j < 0: return
            if i>= rows or j >= cols: return
            if (i,j) in visited: return 
            if heights[i][j] < prevHeight: return
            
            visited.add((i,j))
            
            dfs(i-1,j,visited,heights[i][j])
            dfs(i+1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
            
            
        
        for r in range(0,rows):
            # first col
            dfs(r,0,pac,heights[r][0]) 
            # last col
            dfs(r,cols-1,atl,heights[r][cols-1])

        for c in range(0,cols):
            # first row
            dfs(0,c,pac,heights[0][c])
            # last row
            dfs(rows-1,c,atl,heights[rows-1][c])

        for x,y in atl.intersection(pac):
            solution.append([x,y])
            
        
        return solution