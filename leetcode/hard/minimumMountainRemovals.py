# 1671. Minimum Number of Removals to Make Mountain Array

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        dp1 = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j] and dp1[j] + 1 > dp1[i]:
                        dp1[i] = dp1[j]+1
                            
        dp2 = [1 for _ in nums]
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i-1,-1):
                if nums[i] > nums[j] and dp2[j] + 1 > dp2[i]:
                        dp2[i] = dp2[j]+1
        
      
        ans = 0
        for i in range(len(nums)):
            if dp1[i]!=1 and dp2[i]!=1:
                ans = max(ans,dp1[i]+dp2[i]-1)
        
        return len(nums)-ans
            

        