class Solution:
    def countDistinct(self, s: str) -> int:
        
        substrings = {}
        
        for i in range(0,len(s)):
            for j in range(0,len(s)):
                
                if i+j < len(s):
                    substring = s[i:i+j+1]
                    if substring not in substrings:
                        substrings[substring] = 1
                        
                        
        return len(substrings.keys())
                    
        