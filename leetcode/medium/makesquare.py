# at every step make 4 recursive calls
# to check if the current stick can be placed on the top, right, left or bottom  
# side of the square, 

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if sum(matchsticks) % 4 != 0:
            return False
        
        lengthOfEachSide = sum(matchsticks) // 4
        side = [0]*4
        
        matchsticks.sort(reverse = True)
        
        def helper(index):
            
            if index == len(matchsticks):
                return True
            
            for i in range(4):
                if side[i] + matchsticks[index] <= lengthOfEachSide:
                    side[i] += matchsticks[index] 
                    if helper(index+1):
                        return True
                    side[i] -= matchsticks[index] 
                    
            return False
        
        return helper(0)
 
                
            