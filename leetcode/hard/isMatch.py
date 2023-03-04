# 44. Wildcard Matching


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        def helper(i,j):
            
            key = "{}-{}".format(i,j)
            if key in cache:
                return cache[key]
            
            # both p and s are exhausted    
            if i < 0 and j < 0:
                return True
            
            # p is exhausted and s still has some characters
            # which means p has less characters than s
            if i < 0 and j >= 0:
                return False
            
            # s is exhausted and p still has some characters
            # for s and p to match, p should have * as all
            # the remaining characters, so if there is any other 
            # character other than * then there is a mismatch

            if j < 0 and i >= 0:
                
                for k in range(0,i+1):
                    if p[k] != "*":
                        return False
                    
                return True

            # since ? can be any character, we consider it as a match
            cache[key] = False
            if p[i] == s[j] or p[i] == "?":
                cache[key] = helper(i-1,j-1)
            
            if p[i] == "*":
                cache[key] = helper(i-1,j) or helper(i,j-1)
                
            return cache[key]
            
        
        return helper(len(p)-1,len(s)-1)
            
            
        