class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pointer to even number in odd place
        pointer1 = 0
        # pointer to odd number in even place
        pointer2 = 0
        
        while pointer1 < len(nums) and pointer2 < len(nums):

            while pointer1 < len(nums) and not ( pointer1%2 != 0 and nums[pointer1]%2 == 0 ):
                pointer1+=1
            
            while pointer2 < len(nums) and not ( pointer2%2 == 0 and nums[pointer2]%2 != 0 ):
                pointer2+=1
                    
            if pointer1 != pointer2:
                nums[pointer2],nums[pointer1] = nums[pointer1],nums[pointer2]
                
            pointer1+=1
            pointer2+=1
            
        return nums

class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pointer to even number in odd place
        pointer1 = 0
        # pointer to odd number in even place
        pointer2 = 1
        
        while pointer1 < len(nums) and pointer2 < len(nums):

            
            if nums[pointer1] % 2 == 0:
                pointer1+=2
            elif nums[pointer2] % 2 != 0:
                pointer2+=2
            else:
                nums[pointer2],nums[pointer1] = nums[pointer1],nums[pointer2]

            
        return nums