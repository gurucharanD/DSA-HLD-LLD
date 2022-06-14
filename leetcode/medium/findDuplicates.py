# 442. Find All Duplicates in an Array

# for each element in the array,
# go the index that is pointed by this element 
# and check if this is negative, 
# if it is negative add it into the res array,
# because it is a duplicate element as it already turned negative
# by some other element in the array
# else turn this element into negative

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            
            if nums[abs(nums[i])-1] < 0:
                res.append(abs(nums[i]))
            nums[abs(nums[i])-1]*=-1
            
        return res