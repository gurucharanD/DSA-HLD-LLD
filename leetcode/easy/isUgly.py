class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n == 1:
            return True
        
        while n:
            # since we are taking the division 
            # not the remainder, we need to check
            # if the number has been reduced to 1
            # example :
            # 20 => 2 * (10) => 2 * (2*5) => 2*(2*(5*1))
            if n == 1:
                return True
            
            if n%2==0:
                n = n//2
            elif n%3 == 0:
                n = n//3
            elif n%5 == 0:
                n = n//5
            else:
                return False
            
                
        return False