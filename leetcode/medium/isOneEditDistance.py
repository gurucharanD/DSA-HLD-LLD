class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        if len(t) < len(s):
            s,t = t,s
            
        lens = len(s)
        lent = len(t)
        
        for i in range(lens):
            if s[i] == t[i]:
                continue
            else:
                # if the editdistance is 1
                # when the first mismatch occurs,
                # the remaining part of both the strings 
                # should be same, only then we can say that
                # the edit distance is one

                # if the length is even
                if lens == lent:
                    return s[i+1:] == t[i+1:]
                #  if the length is odd
                #  the string from current index of
                #  smallest string to the end and
                #  index+1 of longest string to the end
                #  should be same
                else:
                    return s[i:] == t[i+1:]
                
        
        return lent-lens == 1
            
        
        
            
            