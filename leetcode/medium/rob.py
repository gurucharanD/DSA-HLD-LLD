# 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # the helper function returns what is the maximum
        # possible profit the robber could make ending at
        # the input index
        
        @lru_cache
        def helper(index):
            if index < 0:
                return 0
            
            if index == 0:
                return nums[0]
            
            if index == 1:
                return max(nums[1],nums[0])
            
            # return max( nums[index] + helper(index-2),nums[index-1]+helper(index-3))
            # max of pick and not pick the element at current index

            return max( nums[index] + helper(index-2),helper(index-1))

        
        if len(nums) == 1:
            return nums[0]
        
        return helper(len(nums)-1)