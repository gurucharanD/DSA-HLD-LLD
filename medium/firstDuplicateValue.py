def firstDuplicateValue(array):
    # Write your code here.
	# if(len(array))<2:
	
	maps = {}
	for i in array:
		if i in maps:
			return i
		else:
			maps[i]=i
	
	return -1

			
