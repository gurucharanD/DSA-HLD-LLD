# quick select has an average case of O(n)
# but the worst case could be O(n^2)
# if the pivot element that you are choosing 
# always falls at the end of the array

# we choose the part in which the answer falls 
# and discard the other half and recursively solve the 
# half that we choose, therefore the complexity is O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums)-k
        
        def quickSelect(l,r):
            pivot,p = nums[r],l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]
            
            if p > k: return quickSelect(l,p-1)
            elif p < k: return quickSelect(p+1,r)
            else: return nums[p]
        
        return quickSelect(0,len(nums)-1)
    