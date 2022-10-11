# 78. Subsets
# complexity of each function is O(1)
# and there are 2^n recursion calls in worst case
# so, the time complexity is O(2^n)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        solution  = []
        
        def helper(subset,n,nums,solution):
            
            if n == len(nums):
                copy = subset[:]
                solution.append(copy)
                return
            
            helper(subset,n+1,nums,solution) # dont consider the elemetn n 
            subset.append(nums[n])
            helper(subset,n+1,nums,solution) # consider the element n
            subset.pop()
            
        helper([],0,nums,solution)
        return solution

            
        