def minimumCharactersForWords(words):
    # Write your code here.
	totalWords = {}
	output = []
	for word in words:
		countOfEachWord = getCountOfCharsForEachChar(word)
		for char in countOfEachWord:
			if char in totalWords:
				totalWords[char] = max(totalWords[char],countOfEachWord[char])
			else:
				totalWords[char] = countOfEachWord[char]
				
	for word in totalWords:
		count = 0
		while count < totalWords[word]:
			output.append(word)
			count+=1
			
    return output


def getCountOfCharsForEachChar(word):
	count = {}
	
	for char in word:
		if char in count:
			count[char]+=1
		else:
			count[char]=1
			
	return count