# reverse the input string  and find the longest common subsequence
# between the input string and the reverse of input string 

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s1 = s
        s2 = s[::-1]
        
        p1 = len(s1)-1
        p2 = len(s2)-1
        
        cache = {}
        def helper(p1,p2):
            key = "{}-{}".format(p1,p2)
            if key in cache:
                return cache[key]
            
            if p1<0 or p2<0:
                return 0
            
            ans = 0
            if s1[p1] == s2[p2]:
                ans = max(ans,1+helper(p1-1,p2-1))
            else:
                ans = max(ans, helper(p1-1,p2), helper(p1,p2-1))
            
            cache[key] = ans
            return ans
        
        return helper(len(s)-1,len(s)-1)
                

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        s1 = s
        s2 = s[::-1]
        
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]
        
        
           
        