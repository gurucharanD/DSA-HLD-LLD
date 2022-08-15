# The max value to xor with the current xor is obtained by 
# the xor of the max value of k

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        xor = [i for i in nums]
        for i in range(1,len(nums)):
            xor[i] = xor[i-1] ^ nums[i]
            
        sol = []
        for p in xor:
            k = p^ pow(2,maximumBit)-1
            print(k)
            sol.append(k)
        
        return sol[::-1]
            
        
        
        
        