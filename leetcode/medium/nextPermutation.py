# start looping from backwards,
# you will find an increasing sequence in the numbers
# [2,1,5,4,3,0,0]
# this loop breaks at 1, since it is at index 1
# our index1 becomes 1

# stop and note the index where the increasing sequence breaks
# and make a note of this index call it index1

# if index1 becomes 0 this means that this input is the last permutation 
# and the next permutation of this input will be first permuation which is 
# all the numbers in asc sorted order

# start looping from backwards again and 
# find the index where the element is greater than the element at index1
# in our example this is 3 and it is at index 4
# and call this index as index2
# after you find these elements swap elements at index1 and index2
# example becomes [2,3,5,4,1,0,0]

# after swapping these elements, reverse the elements from index1+1 to the last
# [2,3,0,0,1,4,5]
# Time : O(N)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index1 = len(nums)-1
        
        while index1 > 0 and nums[index1-1] >= nums[index1]:
            index1-=1
                  
        if index1 == 0:
            nums.sort()
            return 
        
        index1-=1 
            
        index2 = len(nums)-1
        
        while index2 > index1 and nums[index2] <= nums[index1]:
            index2-=1
        
        nums[index1],nums[index2] = nums[index2],nums[index1]
        nums[index1+1:] = nums[index1+1:][::-1]
        
        return nums
        