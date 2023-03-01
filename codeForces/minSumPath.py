def minSumPath(grid):
    
    rows = len(grid)
    cols = len(grid[0])

    dp = [[-1]*cols for _ in range(rows)]

    def helper(r,c):
        if r == 0 and c == 0:
            return grid[r][c]
        
        if r < 0 or c < 0:
            return sys.maxsize
        
        if dp[r][c] != -1:
            return dp[r][c]
        
        dp[r][c] = grid[r][c] + min(helper(r-1,c),helper(r,c-1))
        return dp[r][c]
    
    return helper(rows-1,cols-1)


def minSumPath(grid):
    
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):

            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        
    return dp[rows-1][cols-1]


def minSumPath(grid):
    
    rows = len(grid)
    cols = len(grid[0])

    prev = [0]*cols

    for i in range(0,rows):
        curr = [0]*cols
        for j in range(0,cols):

            if i == 0 and j == 0:
                curr[j] = grid[i][j]
            else:
                left = grid[i][j]
                if j > 0:
                    left = curr[j-1] + left
                else:
                    left = float("inf")
                
                top = grid[i][j]
                if i > 0:
                    top = prev[j] + top
                else:
                    top = float("inf")

                curr[j] = min(top,left)

        prev = curr
    return prev[cols-1]

