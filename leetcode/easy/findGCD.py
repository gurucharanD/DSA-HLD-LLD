# EUCLIDS
# time : O(logN) assuming small number is 2 and largest number is the max number
# approx, less than that in majority of the cases

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        smallest = nums[0]
        largest = nums[len(nums)-1]
        
        def gcd(divisor,dividend):
            
            if divisor == 0:
                return dividend
            
            remainder = (dividend%divisor)
            return gcd(remainder,divisor)
        
        return gcd(smallest,largest)