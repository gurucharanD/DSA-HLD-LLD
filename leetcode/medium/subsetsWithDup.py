# the combinations should be in the sorted order
# inorder to have the duplicates side by side
# we need to sort the input array at the begining
# hence sort the input array before you create the combinations
# to avoid duplicates, you need to consider all the elements
# to be the starting element in the subset array
# if two adjacent elements in the candidate array are equal
# include the first one and dont include the second one
# and keep iterating over the array from current index to last index
# and keep backtracking

# time: O(2^N * N) = deep copy takes a N time
# space: O(2^N * K) = you create 2 pow N subsets and each has a size of avg size of K
# N is the max, 0 is the min

# explanation for condition in line no : 44
# consider the array [1,2,2]
# the elements at index 1 and index 2 are eqaul
# if i consider the element at index 2
# then a duplicate subset [1,2] will be created with 
# index [0,1] and [0,2] this happens because 
# the element at index 1 has already created a subset and
# using the same element again will create a duplicate subset
# to avoid this situation only consider the first occurence
# of the duplicate elements to add into your subsets
# and ignore the remaining occurences
# for better understanding check out the recursion tree 
#  https://leetcode.com/problems/subsets-ii/solution/

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
        
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        temp = []
        
        for num in nums:
            
            i = bisect_left(temp,num)
            if i == len(temp):
                temp.append(num)
            else:
                temp[i] = num
        
        return len(temp)
        