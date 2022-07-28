# when you want the elements in the array only once
# one approach that we can follow is to keep track of the count and 
# we need to keep decremeting the count every time we use a element
# and increment the count back when you back track

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sol = []
        count = {}
        
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
            
        def helper(subset):
            if len(subset) == len(nums):
                sol.append(subset[:])
                return
            
            for num in count:
                if count[num] == 0:
                    continue
            
                subset.append(num)
                count[num] -=1
                helper(subset)
                subset.pop()
                count[num] +=1
            
            return
        
            
        helper([])
        return sol
        