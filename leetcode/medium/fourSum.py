class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)-1
        sol = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                
                newTarget = target - (nums[i]+nums[j])
                
                low = j+1
                high = n
                arr = []
                while low < high:
                    
                    two_sum = nums[low]+nums[high]
                    
                    if two_sum > newTarget:
                        high-=1
                    elif two_sum < newTarget:
                        low+=1
                    else:
                        arr = [nums[i],nums[j],nums[low],nums[high]]
                        if arr not in sol:
                            sol.append(arr)
                        low+=1
                        high-=1
        
        return sol
        