class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def helper(index,target):
            key = "{}-{}".format(index,target)
            if key in cache:
                return cache[key]
            
            if target == 0:
                return 1
            if target < 0:
                return 0
                
            take = 0
            
            for num in nums:
                if num <= target:
                    take += helper(index,target-num)
            
            cache[key] = take
            return take
        
        return helper(len(nums)-1,target)