# 416. Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        cache = {}
        totalSum = sum(nums)
        
        if totalSum & 1:
            return False
        
        targetSum = totalSum >> 1
        
        count = 0
        
        def helper(currSum,index):
            
            key = "{}-{}".format(currSum,index)
            if key in cache:
                return cache[key]
            
            if currSum == 0:
                return True            
            if index < 0:
                return False
            
            pos = helper(currSum,index-1)
            if currSum-nums[index] >= 0:
                pos = pos | helper(currSum-nums[index],index-1)
            
            cache[key] = pos
            return cache[key]
        
        return helper(targetSum,len(nums)-1)
    
            
                
            
        
        