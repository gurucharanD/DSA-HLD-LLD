# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# Repeat and Missing Number Array


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        hashMap = {}
        sol = []
        
        for num in A:
            if num in hashMap:
                sol.append(num)
            else:
                hashMap[num] = 1
        
        for i in range(1,len(A)+1) :
            if i in hashMap:
                continue
            else:  
                sol.append(i)
                break

                           
        
        
        return sol
