from functools import lru_cache

def minimumPathSum(triangle, n):
    
    rows = n
    cols = len(triangle[-1])

    dp = [[-1]*cols for _ in range(n)]
    
    def helper(r,c):
        if r == n-1:
            return triangle[r][c]
            
        if dp[r][c] != -1:
            return dp[r][c]
        
        dp[r][c] = triangle[r][c] + min(helper(r+1,c),helper(r+1,c+1))
        return dp[r][c]

    return helper(0,0)


def minimumPathSum(triangle, n):
    
    cols = len(triangle[-1])

    dp = [[0]*cols for _ in range(n)]

    for i in range(cols):
        dp[-1][i] = triangle[-1][i]
    
    for i in range(n-2,-1,-1):
        for j in range(0,len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j],dp[i+1][j+1])
    
    return dp[0][0]


def minimumPathSum(triangle, n):
    
    cols = len(triangle[-1])

    prev = [0]*cols

    for i in range(cols):
        prev[i] = triangle[-1][i]
    
    for i in range(n-2,-1,-1):
        curr = [0]*cols
        for j in range(0,len(triangle[i])):
                curr[j] = triangle[i][j] + min(prev[j],prev[j+1])

        prev = curr
    return prev[0]