# the element that occurs only once in the array always stands at the even index
# so always keep checking on the even indexes
# if the elemene at index mid is equal to the element at mid+1
# go to the right making low = mid+2
# else go to the left making high = mid

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums)-1
        
        while low < high:
            
            mid = low + (high-low)//2
            
            if mid & 1:
                mid -= 1

            # if mid lands at an odd index
            # we move mid to backward by 1 index
            # by doing a mid-1
            # we do this because the non duplicate number 
            # can only lie in the even index
            # and also the numbers that are before our mid have to be
            # duplicate elements since the number of elements before mid is even
            # 
            
            if nums[mid] == nums[mid+1]:
                low = mid+2
            else:
                high = mid
                
        return nums[low]