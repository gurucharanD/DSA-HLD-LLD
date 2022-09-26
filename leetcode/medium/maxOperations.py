# 1679. Max Number of K-Sum Pairs

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        
        low = 0
        high = len(nums)-1
        count = 0
        
        while low < high:
            sum = nums[low]+nums[high]
            if  sum == k:
                count+=1
                low+=1
                high-=1
            elif sum < k:
                low += 1
            else:
                high -= 1
        
        return count