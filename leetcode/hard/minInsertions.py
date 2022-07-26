# If we know the longest palindromic sub-sequence is x and the length of the string is n then, 
# what is the answer to this problem? It is n - x as we need n - x insertions to make the remaining characters also palindrome.

# this works because we keep the palindromic part of the string intact
# and we need to need add new chars that are not part of the palindrome
# to balance the characters

class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        s1 = s
        s2 = s[::-1]
        
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return len(s)-dp[-1][-1]
        