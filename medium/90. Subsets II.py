# 90. Subsets II

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        def helper(subset,n,nums,solution):
            
            if n == len(nums):
                copy = subset[:]
                copy.sort()
                if copy not in solution:
                    solution.append(copy)
                return
            
            helper(subset,n+1,nums,solution)
            subset.append(nums[n])
            helper(subset,n+1,nums,solution)
            subset.pop()
            
        helper([],0,nums,solution)
        
        return solution
        
        
# O(NlogN*2^N)