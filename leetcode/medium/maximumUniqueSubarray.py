# 1695. Maximum Erasure Value
# sliding window using set to track visited values

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        left = 0
        hashSet = set()
        maxSum = float("-inf")
        total = 0
        for right in range(0,len(nums)):

            while nums[right] in hashSet and left < right:
                hashSet.remove(nums[left])
                total -= nums[left]
                left+=1
            
            total += nums[right]
            hashSet.add(nums[right])
            maxSum = max(maxSum,total)
            
        return maxSum            
            
                
        