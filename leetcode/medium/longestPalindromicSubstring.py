# 5. Longest Palindromic Substring

# assume that the first character in the given string is our longest palindrome
# starting from index 1 at every index
# we need to find the even length palindrome which is string[i-1] to sting[i]
# and we also need to find the odd length palindrome which is string[i-1] to string[i+1]

# then we identify the longest palindrome amongst these
# by expanding outwards i.e decrement left until its greater than 0
# increment right until right is less than the length of the string
# and at every step verify if character at left and right pointers are same
# at the end we return the max palindrome

def longestPalindromicSubstring(string):

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

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return longestPalindromicSubstring(s)
        
        

			