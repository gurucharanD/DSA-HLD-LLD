# permuatation is arraning the elements in the input array in different order
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] for [1,2,3]
# you can have any element in the given array as the first element in the array
# hence you loop through the array and keep a track of which element has been added to the subset
# if the element at the current index in loop is not added to the subset
# you add that element to the subset and when the length of the subset is equal to the length of
# the input array we have generated a valid permuatation and you add that permuatation to the solution
# in the end return the Solution that has all the permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        
        def helper(subset,track):
            
            if len(subset) == len(nums):
                sol.append(subset[:])
                return
            
            for i in range(len(nums)):
                
                if not track[i]:
                    subset.append(nums[i])
                    track[i] = True
                    helper(subset,track)
                    subset.pop()
                    track[i] = False
            
            return
        
        track = {}
        for i in range(0,len(nums)):
            track[i] = False 
        helper([],track)
        return sol


