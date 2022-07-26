class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        s = [None for _ in nums]
        dp = [1 for _ in nums]
        maxIndex = 0
        nums.sort()

        for i in range(1,len(nums)):
            for j in range(0,i):
                
                if nums[i]%nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j]+1
                    s[i] = j
        
            if dp[i] >= dp[maxIndex]:
                maxIndex = i
        
        sequence = []
        while maxIndex is not None:
            sequence.append(nums[maxIndex])
            maxIndex = s[maxIndex]
        return sequence