class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        cache = {}
        def dfs(i,j,count):
            
            if i<0 or i>=m: return 1
            if j <0 or j>=n: return 1
            if count == 0: return 0
            
            key = "{}-{}-{}".format(i,j,count)
            if key in cache:
                return cache[key]

            cache[key] = dfs(i-1,j,count-1)+dfs(i+1,j,count-1)+dfs(i,j+1,count-1)+dfs(i,j-1,count-1)
            return cache[key]%(pow(10,9)+7)
            
        return dfs(startRow,startColumn,maxMove)
        