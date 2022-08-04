# KADANE's ALGORITHM
# 53. Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = nums[0]
        totalMax = nums[0]
        
        for i in range(1,len(nums)):
            currMax = max(currMax+nums[i],nums[i])
            totalMax = max(currMax,totalMax)
        return totalMax