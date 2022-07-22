class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache
        def helper(i,j):
            if i == 0 or j == 0:
                return 1
            
            if i<0 or j <0 :
                return 0
            
            return helper(i-1,j)+helper(i,j-1)
        
        return helper(m-1,n-1)
        