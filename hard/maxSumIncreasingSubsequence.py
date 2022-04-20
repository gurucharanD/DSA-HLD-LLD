# O(n^2) time and O(n) space

def maxSumIncreasingSubsequence(array):
    # Write your code here.
	sums = [num for num in array]
	sequences = [None for _ in array]
	maxSumIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(i):
			otherNum = array[j]
			
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum
				sequences[i] = j
				
		
		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i
				
		
	return [sums[maxSumIdx],buildSequnce(array,sequences,maxSumIdx)]
				
				
			
def buildSequnce(array,sequences,maxSumIdx):
	sequence = []
	while maxSumIdx is not None:
		sequence.append(array[maxSumIdx])
		maxSumIdx = sequences[maxSumIdx]
	
	return list(reversed(sequence))