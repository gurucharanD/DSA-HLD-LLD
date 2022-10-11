def firstNonRepeatingCharacter(string):
    # Write your code here.
	count = {}
	for char in string:
		if char in count:
			count[char]+=1
		else:
			count[char]=1
		

	for i in range(len(string)):
		if count[string[i]] == 1:
			return i
	
		
	
	
    return -1
