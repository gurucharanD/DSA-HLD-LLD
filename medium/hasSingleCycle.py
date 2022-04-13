def hasSingleCycle(array):
    # Write your code here.
	
	visited = {}
	index = 0
	indexValue = array[0]
	
	while index >= 0 and index < len(array)-1:
		nextIndex = index + array[index]
		
		if nextIndex > len(array)-1:
			index = nextIndex % len(array)
		elif nextIndex < 0:
			index = len(array) - nextIndex % len(array)
			
		if nextIndex in visited:
			return false
	
	return False
	