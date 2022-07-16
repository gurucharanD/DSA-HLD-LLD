# Longest Increasing subsequence
# top down

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [-1 for _ in nums]
        
        def helper(n): # represents the LIS ending at index n
            
            if dp[n] != -1: return dp[n]
            ans = 1
            for j in range(n):
                if nums[j] < nums[n]:
                    ans = max(ans,helper(j)+1)
            dp[n]=ans
            return dp[n]
        
        ans  = 1
        for i in range(len(nums)): 
            ans = max(ans,helper(i))
        
        return ans


#bottom up 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        dp = [1 for _ in nums]
        
        for i in range(len(nums)):
            for j in range(0,i):
                
                if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                    dp[i] = 1+dp[j]
                    
        print(dp)
        return max(dp)
        
        
        
                    