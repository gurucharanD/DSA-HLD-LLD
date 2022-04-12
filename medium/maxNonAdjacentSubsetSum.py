# solution1: O(n) time and space

# using the dynamic programming approach
# we create a array that holds the max subset sum that is possible
# at each element in the array. 
# at each index we may or may not include the element at that
# particular index

# recurrence realtion = maxSums[i] = max( maxSums[i-1], maxSums[i-2]+array[i] )



def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	
	if len(array) == 0:
		return 0
	
	if len(array) == 1:
		return array[0]
	
	maxSums = [None]*len(array)
	
	maxSums[0] = array[0]
	maxSums[1] = max(array[0],array[1])
	
	for i in range(2,len(array)):
		maxSums[i] = max(maxSums[i-1],maxSums[i-2]+array[i])
		
	return maxSums[-1]
	
# solution 2: 
# space can be improved, so instead of saving all the maxSums 
# we just save the last two max sums possible
# and we update the values of these sums at each step

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
		
	if len(array) == 0:
		return 0
	
	if len(array) == 1:
		return array[0]
	
	sumOne = array[0]
	sumTwo = max(array[0],array[1])
	
	maxSum = max(sumOne,sumTwo)
	
	for i in range(2,len(array)):
		maxSum = max( sumTwo, sumOne + array[i] )
		
		sumOne = sumTwo
		sumTwo = maxSum
		
	return maxSum
		
		
