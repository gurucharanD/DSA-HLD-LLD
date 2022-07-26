class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        daysCovered  = {
            0:1,
            1:7,
            2:30
        }
        cache = {}
        def helper(index):
            if index in cache:
                return cache[index]
            
            if index == len(days):
                return 0
            
            minCost = float("inf")
    
            for j in range(0,len(costs)):
                cost = costs[j]
                noOfDaysCoverd = days[index]+daysCovered[j]-1
                
                i = index+1
                while i < len(days) and days[i] <= noOfDaysCoverd:
                    i+=1
                
                nextCost = helper(i)
                minCost = min(minCost,cost+nextCost)

            cache[index] = minCost
            return minCost
            
        return helper(0)
            
                        
                
                
            
                
                