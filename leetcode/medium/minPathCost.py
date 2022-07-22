

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        
        dp = [ [float("inf") for _ in range(0,len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(0,len(grid[0])):
            dp[0][i] = grid[0][i] 
            
        for i in range(1,len(dp)):
            for j in range(0,len(dp[0])):
                
                prevRow = i-1
                currentNode = grid[i][j]
                
                for colIndex in range(0,len(dp[0])):
                    
                    prevNode = grid[prevRow][colIndex]
                    cost = moveCost[prevNode][j]
                                        
                    dp[i][j] = min(dp[i][j], grid[i][j]+dp[prevRow][colIndex]+cost)
                    
        return min(dp[-1])

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        def helper(i,j):
            if i == len(grid)-1:
                return grid[i][j]
            
            rowLevel = 0
            for row in range(i,i+1):
                ans = float(inf)

                for col in range(0,len(grid[0])):

                    currentNode = grid[row][col]
                    for index in range(0,len(grid[0])):
                        cost = moveCost[currentNode][index]
                        costToNextLevel = helper(i+1,index)
                        # print(currentNode,cost,ans,costToNextLevel)
                        ans = min(ans,currentNode+cost+costToNextLevel)
                rowLevel+=ans
                print(rowLevel)
            return ans
                    
        return helper(0,0)
                    
                    
            
        
        