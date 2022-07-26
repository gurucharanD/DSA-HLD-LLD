# 44. Wildcard Matching


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        def helper(i,j):
            
            key = "{}-{}".format(i,j)
            if key in cache:
                return cache[key]
            
            if i < 0 and j < 0:
                return True
            
            if i < 0 and j >= 0:
                return False
            
            if j < 0 and i >= 0:
                
                for k in range(0,i+1):
                    if p[k] != "*":
                        return False
                    
                return True

            cache[key] = False
            if p[i] == s[j] or p[i] == "?":
                cache[key] = helper(i-1,j-1)
            
            if p[i] == "*":
                cache[key] = helper(i-1,j) or helper(i,j-1)
                
            return cache[key]
            
        
        return helper(len(p)-1,len(s)-1)
            
            
        