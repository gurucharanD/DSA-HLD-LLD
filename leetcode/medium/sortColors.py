# Three pointer approach
# when you find a 0 swap it with low pointer
# when you find a 2 swap it with high pointer
# when you find a 1 just increment mid pointer

class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        
        low = 0 
        mid = 0
        high = len(arr)-1
        
        while mid <= high:
            
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid] == 2:
                arr[high],arr[mid] = arr[mid],arr[high]
                high-=1
                # in this case we dont move the mid pointer because 
                # if you are swapping a zero at last pointer 
                # to 2 at mid pointer
                # the 0 should be swapped with low pointer
                # to keep a check on the swapped value
                # we keep the mid unmoved
            else:
                mid+=1
        
        