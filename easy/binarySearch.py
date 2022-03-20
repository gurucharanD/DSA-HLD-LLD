import math
def binarySearch(array, target):
    # Write your code here.
 	return binarySearchHelper(array,0,len(array)-1,target)
    


def binarySearchHelper(array,left,right,target):
	
	if right < left:
		return -1
	
	mid = (left+right)//2
	if array[mid] == target:
		return mid
	
	elif array[mid] > target:
		right = mid - 1;
	else:
		left = mid + 1;
	
	return binarySearchHelper(array,left,right,target)
	
	
	