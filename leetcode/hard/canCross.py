class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        stonesCache  = {}
        
        for i in range(len(stones)):
            stonesCache[stones[i]] = i
                
        cache = {}
        
        def helper(index,k):
                
            if (index,k) in cache:
                return cache[(index,k)]
            
            if index == len(stones)-1:
                return True
                                    
            if stones[index]+k in stonesCache:
                index = stonesCache[stones[index]+k]
                
                res1 = False
                if k-1 is not 0:
                    res1 = helper(index,k-1)
                    
                res2 = False
                if k+1 < len(stones):
                    res2 = helper(index,k+1)
                    
                cache[(index,k)] = (
                    res2 or 
                    helper(index,k) or 
                    res1
                )
                return cache[(index,k)]

            return False
        
        return helper(0,1)