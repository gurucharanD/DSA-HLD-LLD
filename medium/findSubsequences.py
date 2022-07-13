class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        sol= []
        def helper(subset,index):
            
            if index >= len(nums):
                if len(subset) > 1 and subset not in sol:
                    sol.append(subset[:])
                return
            
            helper(subset,index+1)
                                
            if len(subset) == 0 or nums[index] >= subset[-1]:
                subset.append(nums[index])
                helper(subset,index+1)
                subset.pop()
            
        helper([],0)
        return sol
                