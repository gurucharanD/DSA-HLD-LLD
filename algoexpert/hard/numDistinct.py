# try out all the possibilites of comparing string s and string t
# start at the end of the strings and comapre character by character
# if you find a match 
#     you have two options
#     you can consider the current character as a match 
#     in this case you do i-1 and j-1
#     or you dont want to consider the character as a match
#     in this case you do i-1 and stay at j
#     return the sum of both the options
# else
    # you have no option but go forward
    # by doing i-1 and j-1

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}
        def helper(i,j):
            key = "{}-{}".format(i,j)
            if key in cache:
                return cache[key]
            
            if j < 0:
                return 1
            if i < 0:
                return 0
            
            
            if s[i] == t[j]:
                cache[key] = helper(i-1,j-1)+helper(i-1,j)
            else:
                cache[key] = helper(i-1,j)
            
            return cache[key]
            
        return helper(len(s)-1,len(t)-1)
        