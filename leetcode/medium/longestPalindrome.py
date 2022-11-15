# The intuition is to categroise the words into two types 1. where both the chars are same 2.both the chars are different
# in case 1, we will have multiple cases depending on the length of the palindrome formed thus far:
# if this can be broken down into two equal halfs then we can add all the occurences of the
# current word into palindrome. (i.e add some at the ends of the palindrome and few at the middle )
# else we can only append the current word at the begining and end ( the count should be atleast 2 to do this)
# in case 2, we append the min of count of current word and its reverse and multiply it by 2

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        length = 0
        
        counter = Counter(words)
            
        for word in counter:
            rev_word = word[::-1]
            # print(word,rev_word)
            if word == rev_word:
                if length == 0:
                    length += counter[word]*2
                else:
                    half = length/2
#                   if current palindrome can be broken into two even halfs
#                   then i can take add all the words into my palindrome
                    if half % 2 == 0:
                        length += counter[word]*2
                    else:
                    # else only even number of words can be added
                        if counter[word] % 2:
                            length += (counter[word] -1) * 2
                        else:
                            length += counter[word]*2

            else:
                if rev_word in counter and counter[rev_word]: 
                    length += min(counter[word],counter[rev_word])*4
                    counter[rev_word] = 0
            
        return length 