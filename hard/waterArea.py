# O(n) time and sapce

def waterArea(buildings):
    # Write your code here.
	leftTallestPillarHeights = [0 for _ in buildings]
	rightTallestPillarHeights = [0 for _ in buildings]
	
	maxTallSoFar = 0
	
	# identify the left tallest pillar to each pillar
	for i in range(1,len(leftTallestPillarHeights)):
		leftBuildingHeight = buildings[i-1]
		leftTallestPillarHeights[i] = max(maxTallSoFar,leftBuildingHeight)
		
		if leftBuildingHeight > maxTallSoFar:
			maxTallSoFar = leftBuildingHeight
			
	# identify the right tallest pillar to each pillar
	maxTallSoFar = 0
	for j in range(len(buildings)-2, -1, -1):
		rightBuldingHeight = buildings[j+1]
		rightTallestPillarHeights[j] = max( rightBuldingHeight, maxTallSoFar)
		
		if rightBuldingHeight > maxTallSoFar:
			maxTallSoFar = rightBuldingHeight
		
	print(leftTallestPillarHeights,rightTallestPillarHeights)
	
	# water = [0 for _ in range(len(buildings))]

    # the amount of water captured on any building is the 
    # difference between the min of the tallest buildings
    # to the left and right of the current building and 
    # its height 

	sum = 0
	
	for i in range(0,len(buildings)):
		height = buildings[i]
		minHeight = min(leftTallestPillarHeights[i],rightTallestPillarHeights[i])
		
		if height < minHeight:
			sum+= abs(height-minHeight)
				
		
	return sum
		
		
		
		
		
