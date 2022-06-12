# 1658. Minimum Operations to Reduce X to Zero
# change the target from x to sum(nums) - x
# and find the longest subarray that consitiutes the value sum(nums) - x
# the difference between the length of the above array and length of nums gives
# the min operations to reduce x to zero

# find prefix sum of the array and  save the prefix sum in hashMap 
# indexed by the prefix sum as key and index is the value
# at every iteration find prefixSum at that index - target
# if that difference exists in the hashMap, 
# find the length of the subarray by 
# the difference between the indices and keep trakck of the maxLength subarray


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
        target = sum(nums) - x
        prefixSumHashMap = {}
        prefixSumHashMap[0] = -1
        maxLenSubArray = -1
        
        prefixSum = 0
        for i in range(0,len(nums)):
            prefixSum+=nums[i]
            prefixSumHashMap[prefixSum] = i
            diff = prefixSum - target
            
            if diff in prefixSumHashMap:
                currSubArrayLength = i - prefixSumHashMap[diff]
                maxLenSubArray = max(maxLenSubArray,currSubArrayLength)
                
        
        if maxLenSubArray == -1:
            return maxLenSubArray
        else:
            return len(nums) - maxLenSubArray
                
                
        
    
