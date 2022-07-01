# 462. Minimum Moves to Equal Array Elements II
# The middle number in the sorted array is ( hypothetically ) equidistant from the remaining numbers in the array
# find the middle number and sum the difference of all the numbers to it
# return the sum
# O(nlogn) time and O(1) space

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        
        index = (0 + len(nums) )//2
        
        number = nums[index]
        
        count = 0
        
        for i in nums:
            count+=abs(number-i)
        
        return count
        
        