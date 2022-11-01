# 523. Continuous Subarray Sum

# if two sub array sums
# generate same remainder for the prefix sum % k
# then we can say that there is a subarray with 
# sum that is a multiple of K

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        lookUp ={0:-1}
        cumilative_sum = 0
        
        for idx,num in enumerate(nums):
            
            cumilative_sum += num
            remainder = cumilative_sum % k
            
            if remainder in lookUp :
                if idx - lookUp[remainder] >= 2:
                    return True
            else:
                lookUp[remainder] = idx
                
        return False
            
            
            