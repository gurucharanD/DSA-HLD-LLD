# sort the input array by one dimension at the begingin of the problem
# using dynamic programming, keep track of the maximum  height of
# the stack that could be built at each step in an array

# at every step in the disks, the maximum height 
# of the stack that can be build is equal to the height of
# that particular disk

# so, for each disk, compare all the disks previous to the current disk and 
# see the maximum height that could be built using the disks visited so far

def diskStacking(disks):
    # sort the disks by height first
	disks.sort(key = lambda disk:disk[2])
	heights = [x[2] for x in disks]
	sequences = [None for _ in disks]
	for i in range(1,len(disks)):
		currentDisk = disks[i]
		for j in range(0,i):
			if disks[i][0] > disks[j][0] and disks[i][1] > disks[j][1] and disks[i][2] > disks[j][2] and heights[i] < heights[j] + currentDisk[2]:
				heights[i] = currentDisk[2]+heights[j]
				sequences[i] = j
				
	maxHeightIndex = 0
	for i in range(1,len(heights)):
		if heights[i] > heights[maxHeightIndex]:
			maxHeightIndex = i
		
	sequence = []
	currentIndex = maxHeightIndex
	while currentIndex is not None:
		sequence.append(disks[currentIndex])
		currentIndex = sequences[currentIndex]
	
	return list(reversed(sequence))



