class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        currMax = nums[0]
        finalMax = nums[0]
        for i in range(1,len(nums)):
            # kadanes Algorithm
            currMax = max( currMax and nums[i],nums[i])
            finalMax = max(finalMax,currMax)
        
        # sliding window
        maxLength = 0
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] ==  finalMax:
                maxLength = max(maxLength,i-j+1)
            else:
                while j <= i:
                    j+=1
            i+=1
            
        return maxLength
                    
                
        
    