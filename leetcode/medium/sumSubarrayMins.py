# 907. Sum of Subarray Minimums
# 
# using monotonic stack 
# and the concept of 
# finding the smallest number to the right 
# and the smallest number to the left
# this gives us the range or the number of sub arrays
# the current element is a min of the sub array
# 
#   left = abs(i-left_range[i])
#   right = abs(i-right_range[i])        
#   res += (arr[i]*left*right) 

class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        left_range = [-1]*len(arr)
        right_range = [len(arr)]*len(arr)
        
        # find index with smaller or equal element
        # to the right of current index     
        stack = []
        for i in range(0,len(arr)):
            
            while stack and arr[stack[-1]] >= arr[i]:
                right_range[stack.pop()] = i
            
            stack.append(i)
        
        # find index with smaller or equal element
        # to the left of current index        
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                left_range[stack.pop()] = i
            stack.append(i)
            

        res = 0
        for i in range(len(arr)):
            left = abs(i-left_range[i])
            right = abs(i-right_range[i])
            
            res += (arr[i]*left*right) 
        
        return res% (pow(10,9)+7)
        
        