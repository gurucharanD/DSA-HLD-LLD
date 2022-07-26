class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp1 = [1 for _ in nums]
        count = [1 for _ in nums]
        maxi = 1
        for i in range(len(nums)):
            prevCount  = 1
            for j in range(0,i):
                if nums[i] > nums[j] and dp1[j] + 1 > dp1[i]:
                        dp1[i] = dp1[j]+1
                        count[i] = count[j]
                elif dp1[j] + 1 == dp1[i]:
                        count[i] += count[j]
            
            maxi = max(maxi,dp1[i])
        print(count,maxi)
        
        ans = 0
        for i in range(len(dp1)):
            if dp1[i] == maxi:
                ans+=count[i]
        return ans