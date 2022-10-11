def generateDocument(characters, document):
    # Write your code here.
	lettersInCharCount = {}
	lettersInDocCount = {}
	
	for char in characters:
		if char in lettersInCharCount:
			lettersInCharCount[char] += 1
		else:
			lettersInCharCount[char] = 1
	
		
	for char in document:
		if char in lettersInDocCount:
			lettersInDocCount[char] += 1
		else:
			lettersInDocCount[char] = 1
	
	
	for key in lettersInDocCount:
		if key not in lettersInCharCount or lettersInDocCount[key] > lettersInCharCount[key]:
			return False
		

		
    return True
