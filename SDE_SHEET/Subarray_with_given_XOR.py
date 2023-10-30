from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        seen = {}
        xor = 0
        count = 0
        
        for i in range(len(A)):
            
            xor ^= A[i]
            if xor == B:
                count+=1
            
            y = xor ^ B
            if y in seen:
                count += seen[y]
            
            seen[xor] = seen.get(xor,0)+1
        
        return count    
        
      
        