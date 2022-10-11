# initialise the lengths array to one at the beginning 
# as the min longest subsequence length at any index would be 1
# beacuse the element may be the first element in the subsequence

# for every i and j = 0 and i < j 
# if array[i]>array[j]
# verify if the length of the subsequence at j plus including the 
# current element is greater than the length at the current element

# O(n^2) time and O(n) space

def longestIncreasingSubsequence(array):
	lengths = [1 for _ in array]
	sequences = [None for _ in array]
	maxIndex = 0
	for i in range(len(array)):
		for j in range(0,i):

			if array[i] > array[j] and lengths[j] + 1 > lengths[i]:
					lengths[i] = lengths[j]+1
					sequences[i] = j
			
		if lengths[i] >= lengths[maxIndex]:
			maxIndex = i
			
	sequence = []
	print(maxIndex)
	while maxIndex is not None:
		sequence.append(array[maxIndex])
		maxIndex = sequences[maxIndex]
			
	print(array)
	print(lengths)
	print(sequences)
	print(list(reversed(sequence)))
	
	return list(reversed(sequence))

	
# just to find the longest increasing subsequence length

def longestIncreasingSubsequence(array):
	lengths = [1 for _ in array]
	sequences = [None for _ in array]
	maxIndex = 0
	for i in range(len(array)):
		for j in range(0,i):
			if array[i] > array[j]:
					lengths[i] = max(lengths[j]+1,lengths[i])

			
	return lengths[len(array)-1]

	

	
	