class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        ans = []
        nums.sort()
        
        for i,a in enumerate(nums):
            # [-1,0,1,2,-1,-4] after sorted becomes [-4, -1, -1, 0, 1, 2]
            # to avoid using the same number as first number multiple times
            # we check if the number at current index is equal to the number at
            # index-1, if they are same we ignore the number at index as the same number
            # has been used already at index-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            low,high = i+1,len(nums)-1
            
            while low < high:
                
                add = a + nums[low] + nums[high]
                
                if add < target:
                    low+=1
                elif add > target:
                    high -= 1
                
                else:
                    ans.append([a,nums[low],nums[high]])
                    low += 1
                    # moving the low pointer to the place which
                    # which is a number that is not duplicated
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
        
        return ans
        