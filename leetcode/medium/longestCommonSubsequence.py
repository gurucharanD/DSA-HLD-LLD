class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        p1 = len(text1)-1
        p2 = len(text2)-1
        
        cache = {}
        
        def helper(p1,p2):
            
            key = "{}-{}".format(p1,p2)
            if key in cache:
                return cache[key]
            
            if p1<0 or p2<0:
                return 0
            
            curr = 0
            if text1[p1] == text2[p2]:
                curr = 1
                
            cache[key] =  max(helper(p1-1,p2),helper(p1,p2-1),helper(p1-1,p2-1)+curr)
            return cache[key]
        
        return helper(p1,p2)