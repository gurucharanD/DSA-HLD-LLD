def runLengthEncoding(string):
	char = string[0]
	count = 1
	output = ''
	
	for i in range(1,len(string)):
		if count == 9 or char != string[i]:
			output = output + (str(count)+char)
			char = string[i]
			count = 0
		
		count+=1
		
	
	return output + (str(count)+char)



def runLengthEncoding(string):
	output = ''
	count = 1
	for i in range(len(string)-1):
			
		currentChar = string[i]
		nextChar = string[i+1]
		
		if count == 9 or currentChar != nextChar:
			output = output + (str(count) + currentChar)
			count = 1
		else:
			count += 1
			
		
	return output + str(count) + string[len(string)-1]


