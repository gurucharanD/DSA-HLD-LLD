from functools import lru_cache

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    
    @lru_cache(None)
    def helper(row,c1,c2):

        if (c1 < 0 or c1>=c) or (c2 < 0 or c2 >= c):
            return float("-inf")
        
        if row == r-1:
            if c1 == c2:
                return grid[row][c1]
            else:
                return grid[row][c1]+grid[row][c2]
        
        maxi = 0
        directions = [-1,0,1]
        for i in directions:
            for j in directions:
                if c1 == c2:
                    maxi = max(maxi,grid[row][c1]+helper(row+1,c1+i,c2+j))
                else:
                    maxi = max(maxi,grid[row][c1]+grid[row][c2]+helper(row+1,c1+i,c2+j))
        
        return maxi
    
    return helper(0,0,c-1)


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    
    dp = [[[-1]*c for _ in range(r)] for _ in range(r)]
    def helper(row,c1,c2):

        if (c1 < 0 or c1>=c) or (c2 < 0 or c2 >= c):
            return float("-inf")
        
        if row == r-1:
            if c1 == c2:
                return grid[row][c1]
            else:
                return grid[row][c1]+grid[row][c2]
        
        if dp[row][c1][c2] != -1:
            return dp[row][c1][c2]

        maxi = 0
        directions = [-1,0,1]
        for i in directions:
            for j in directions:
                if c1 == c2:
                    maxi = max(maxi,grid[row][c1]+helper(row+1,c1+i,c2+j))
                else:
                    maxi = max(maxi,grid[row][c1]+grid[row][c2]+helper(row+1,c1+i,c2+j))
        
        dp[row][c1][c2] = maxi
        return dp[row][c1][c2]
    
    return helper(0,0,c-1)

