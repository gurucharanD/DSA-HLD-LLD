# O(n) time and O(1) space
# max sum non-empty sub array elements must be adjacent
# dyanmic programming approach, we find the
# max sum of all the subarrays at each element from 0 to n

# at every step decide, if we could generate a greater sum
# by adding or not adding the element 

# we comapre the max sum thus far plus the currentElement with the currentElement 
# and choose the maximum of these two, sometimes the max sum thus far can can be smaller than the 
# currentElement due to negative numbers before the currentElement and adding the currentElement
# to that max sum thus far is not going to increase the sum, so we start fresh by considering
# the current element as the first element of our sub array (this is what we are doing in line 25)

# and we track the gloabl maximum sub array sum at each step

# recurrence => maxSum[i] = max( maxSum[i-1] + array[i], array[i] )

def kadanesAlgorithm(array):
	
	maxEndingHere = array[0]
	totalMax = array[0]
	for i in range(1,len(array)):
        # counter the negative numbers
		maxEndingHere = max(maxEndingHere+array[i],array[i]) 
		totalMax = max(totalMax,maxEndingHere)
    
	return totalMax

