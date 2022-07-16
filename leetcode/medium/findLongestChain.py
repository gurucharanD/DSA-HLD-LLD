class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key = lambda x:x[0])
                
        dp = [1 for _ in pairs]
        
        for i in range(len(pairs)):
            for j in range(0,i):
                
                if pairs[i][0] > pairs[j][1] and dp[j]+1 > dp[i]:
                     dp[i] = 1+dp[j]
                    
        return max(dp)  