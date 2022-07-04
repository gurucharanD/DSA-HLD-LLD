# 376. Wiggle Subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        inc = 1
        dec = 1
        
        for i in range(1,len(nums)):
            
            if nums[i] > nums[i-1]:
                inc = dec+1
            elif nums[i] < nums[i-1]:
                dec = inc+1
        
        return max(inc,dec)


# didnt work of 2 test cases

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return 1
        
        dp = [1 for _ in nums]
        dp[1] = 2 if nums[0] != nums[1] else dp[0]
        
        prevDiff = nums[1]-nums[0]
        for i in range(2,len(nums)):
            
            currDiff = nums[i]-nums[i-1]
            
            if ( prevDiff <= 0 and currDiff > 0) or ( prevDiff > 0 and currDiff <= 0):
                dp[i] = max( dp[i], 1+dp[i-1] )
            else:
                dp[i] = dp[i-1]
                
            prevDiff = currDiff
        
        print(dp)
        return max(dp)