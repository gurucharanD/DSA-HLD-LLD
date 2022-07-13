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


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        nums.sort()
        def helper(subset,index):
            
            copy = subset[:]
            solution.append(copy)
            
            for i in range(index,len(nums)):
                if i > index and nums[i-1] == nums[i]:
                    continue
                    
                subset.append(nums[i])
                helper(subset,i+1)
                subset.pop()
            
        helper([],0)
        
        return solution
        
        