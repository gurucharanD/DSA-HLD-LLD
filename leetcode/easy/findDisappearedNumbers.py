# update the numbers at nums[index] to negative
# after updating all the numbers in the array
# the indexes which still have the positive numbers 
# are the values that are missing form the input array
# this approach works only because the input array is
# in the range of 1 to len(nums)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # maximum = len(nums)
        # ans = []
        # nums = set(nums)
        # for i in range(1,maximum+1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans
        
        for i in range(len(nums)):
            
            num_index = abs(nums[i])-1
            
            if nums[num_index] > 0:
                nums[num_index]*=-1
        
        res = []
        for i in range(1,len(nums)+1):
            if nums[i-1] > 0:
                res.append(i)
        
        return res
        