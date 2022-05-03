# recursive apporach :
# time = O(k^n) space = O(n)
# draw the recursive tree to understand the time 

# if maxStep = 2
# then noOfWays[2] = noOfWays[1] + noOfWays[0]
# let k = maxStep
# we make K recursive calls at each level
# and we have N such levels i.e O(K^N)

# space is the size of the recursion stack


def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return traversal(height,maxSteps)

def traversal(height,maxSteps):
	
	if height == 0 or height == 1 :
		return 1
	totalWays = 0
	for i in range(1,min(height,maxSteps)+1):
		totalWays += traversal(height-i,maxSteps)
	
	return totalWays

# recursive approach with memoisation
# same time and space except few extra
# calls are removed

def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return traversal(height,maxSteps,{0:1,1:1})

def traversal(height,maxSteps,memoize):
	
	if height in memoize :
		return memoize[height]
	
	totalWays = 0
	for i in range(1,min(height,maxSteps)+1):
		totalWays += traversal(height-i,maxSteps,memoize)
	memoize[height] = totalWays
	return totalWays


# using DP 
# O(N*K) time and O(N) space

def staircaseTraversal(height, maxSteps):
	noOfWays = [0 for _ in range(height+1)]
	noOfWays[0] = 1
	noOfWays[1] = 1
	for i in range(2,height+1):
		step = 1
		while step <= maxSteps and step <= i:
			noOfWays[i] = noOfWays[i] + noOfWays[i-step]
			step+=1
	print(noOfWays)
	return noOfWays[height]


# using sliding window
# time: O(N) and O(N) space
# avoiding overlaps from previous approach
# draw the array to visualise better

def staircaseTraversal(height, maxSteps):
	
	currentNoOfWays = 0
	waysToTop = [1]
	
	for currentHeight in range(1,height+1):
		startOfWindow = currentHeight - maxSteps - 1
		endOfWindow = currentHeight - 1
		
		if startOfWindow >= 0:
			currentNoOfWays -= waysToTop[startOfWindow]
			
		currentNoOfWays += waysToTop[endOfWindow]
		waysToTop.append(currentNoOfWays)
		
	return waysToTop[height]