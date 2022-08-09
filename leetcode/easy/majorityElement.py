# assume first element is the required solution 
# we start looping from index1, we check if the current element is equal to result
# if it is equal, we increment the counter by 1
# else we decrement the counter by 1
# if count becomes less than or equal to 0, it means 
# the current result we have is not the expected answer
# and we need to start fresh from the current index
# assuming the element at current index is the result
# and count of the majority element is 1 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        result = nums[0]
        
        for num in nums:
            if num == result:
                count+=1
            else:
                count -= 1
            
            if count <= 0:
                count = 1
                result = num
                
        return result
        
        
        