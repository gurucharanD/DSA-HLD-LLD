# BRUTEFORCE :
# get all possible substrings and check if this is a palindrome
# and return the longest palindrome it runs with O(n^3) time

# dobule for loop to generate all the substrings
# and another N is for checking if the string is palindrome

def longestPalindromicSubstring(string):
	
	if len(string) == 1:
		return string
	
	lenOfLongestPalindrome = 0
	longestPalindrome = ''
	for i in range(0,len(string)+1):
		for j in range(i+1,len(string)+1):
			currString = string[i:j]
			print(currString)
			if len(currString) > lenOfLongestPalindrome and checkPalindrome(currString):
				# if len(currString) > lenOfLongestPalindrome:
					longestPalindrome = currString
					lenOfLongestPalindrome = len(currString)
		
	return longestPalindrome
		
def checkPalindrome(inputstring):	
	if len(inputstring) == 1:
		return True
	
	pointer1 = 0
	pointer2 = len(inputstring)-1
	
	while pointer1 <= pointer2:
		if inputstring[pointer1] != inputstring[pointer2]:
			return False
	
		pointer1+=1
		pointer2-=1
	
	return True

# __________________________

# at every index, consider the current index as the middle of the palindrome and
# keep expanding in oppposite directions until elements at both the indexes are same. 
# if both the elements are same increment both pointers
# else update the current longest palindrome if the current palindrome length 
# is greater than the one we already know
# this takes O(n^2) time atmost, if the entire string is longest palindrome
# we traverse half the list which an n/2 operation

# we also need to check the even length and odd length palindromes

def longestPalindromicSubstring(string):
    # Write your code here.
	# index,length
	currentLongest = [0,1]
    for i in range(1,len(string)):
		odd = getLongest(string,i-1,i+1)
		even = getLongest(string,i-1,i)
		
		longest = max(odd,even,key=lambda x : x[1] - x[0])
		currentLongest = max(currentLongest,longest,key=lambda x : x[1] - x[0])
		
	
	return string[currentLongest[0]:currentLongest[1]]

def getLongest(string,leftIndex,rightIndex):
	
	while leftIndex >= 0 and rightIndex < len(string):
		if string[leftIndex]!=string[rightIndex]:
			break
		
		leftIndex-=1
		rightIndex+=1
		
	return [leftIndex+1,rightIndex]
			
		
		
