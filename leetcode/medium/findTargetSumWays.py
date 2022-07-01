# 494. Target Sum

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        cache = {}
        
        def helper(index,array,count,target):
            if (index,count) in cache:
                return cache[(index,count)]
            
            if index == len(array):
                if count == target:
                    return 1
                return 0
            

            
            # dont change the sign of the element at current index
            l = helper(index+1,array,count+array[index],target)  
            # change the sign of the element at current index
            r = helper(index+1,array,count-array[index],target)
            
            # cache the response of the current recursive call
            cache[(index,count)] = l+r
            
            return cache[(index,count)]

        
        return helper(0,nums,0,target)



class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        dp = {}
        
        def helper(index,array,target,dp):
            
            if (index,sum(array)) in dp:
                return dp[(index,sum(array))]
            
            if index == len(array):
                if sum(array) == target:
                    return 1                
                return 0
            
            
            l = helper(index+1,array,target,dp)
            array[index]*=-1
            r = helper(index+1,array,target,dp)
            array[index]*=-1
            
            dp[(index,sum(array))] = l+r
            return dp[(index,sum(array))]
        
        return helper(0,nums,target,{})
            
            


            