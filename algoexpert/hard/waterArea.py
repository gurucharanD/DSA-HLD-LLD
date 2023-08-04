# O(n) time and sapce

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        left_max = [0]*n
        right_max = [0]*n

        maxThusFar = 0
        for i in range(1,n):
            left_max[i] = max(height[i-1],maxThusFar)
            maxThusFar = left_max[i]
        
        maxThusFar = 0
        for i in range(n-2,-1,-1):
            right_max[i] = max(height[i+1],maxThusFar)
            maxThusFar = right_max[i]
        
        ans = 0
        for i in range(n):

            curr_hei = height[i]
            min_hei = min(left_max[i],right_max[i])

            if min_hei > curr_hei:
                ans += (min_hei-curr_hei)
        
        return ans
            
        

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
		
		
		
		
		
