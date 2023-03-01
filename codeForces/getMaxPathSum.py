from functools import lru_cache

def getMaxPathSum(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    @lru_cache(None)
    def helper(i,j):

        if j < 0 or j >= cols:
            return float("-inf")
        
        if i == 0:
            return matrix[i][j]
        
        return matrix[i][j] + max(helper(i-1,j),helper(i-1,j-1),helper(i-1,j+1))
    
    ans = float("-inf")
    for j in range(cols):
        ans = max(ans, helper(rows-1,j))
    
    return ans

def getMaxPathSum(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[-1]*cols for _ in range(rows)]

    def helper(i,j):

        if j < 0 or j >= cols:
            return float("-inf")
        
        if i == 0:
            return matrix[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = matrix[i][j] + max(helper(i-1,j),helper(i-1,j-1),helper(i-1,j+1))
        return dp[i][j]
    
    ans = float("-inf")
    for j in range(cols):
        ans = max(ans, helper(rows-1,j))
    
    return ans


def getMaxPathSum(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0]*cols for _ in range(rows)]

    for i in range(cols):
        dp[0][i] = matrix[0][i]
    
    for i in range(1,rows):
        for j in range(cols):

            dp[i][j] = matrix[i][j] + max(
                dp[i-1][j] if i > 0 else float("-inf"),
                dp[i-1][j-1] if i > 0 and j > 0 else float("-inf"),
                dp[i-1][j+1] if i > 0 and j < cols-1 else float("-inf")
            )
    
    return max(dp[-1])

def getMaxPathSum(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    prev = [0]*cols

    for i in range(cols):
        prev[i] = matrix[0][i]
    
    for i in range(1,rows):
        curr = [0]*cols
        for j in range(cols):

            curr[j] = matrix[i][j] + max(
                prev[j] if i > 0 else float("-inf"),
                prev[j-1] if i > 0 and j > 0 else float("-inf"),
                prev[j+1] if i > 0 and j < cols-1 else float("-inf")
            )
        prev = curr
    return max(prev)