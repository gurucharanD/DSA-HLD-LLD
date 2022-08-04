class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        if target <= nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            low = 0
            high = len(nums)-1
            
            while low <= high:
                
                mid = (high+low)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid-1] < target and nums[mid] >= target:
                    ans = mid
                    
                if nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
        
        return ans