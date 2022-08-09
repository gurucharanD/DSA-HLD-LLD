# using binary exponentation
# ex: x = 2, n = 10
# 2^10 = (2^2)^5 = 4^5
# 4^5 = 4* 4^4 = 4 * (4^2)^2 = 16^2
# 16^2 = 256 => 4*256 = 1024
# Time O(logn)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        flag = n < 0
        if flag:
            n *= -1
        ans = 1
            
        nn = n
        while nn != 0:
            if nn % 2 :
                ans *= x
                nn -= 1
            else:
                x *= x
                nn /= 2
        

        if flag:
            return 1/ans
        
        return ans
        