class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}        
        def helper(index,buy):
            
            key = "{}-{}".format(index,buy)
            if key in cache:
                return cache[key]
            
            if index >= len(prices):
                return 0
                         
            profit = 0
            if buy:
                # since you are buying profit is negative
                # since you made the purchase you need to sell the next day
                # you decide not to buy on current day, you can buy on the next day
                profit = max( -prices[index] + helper(index+1,0), helper(index+1,1))
            else:
                # since you are not allowed to buy the stock the next day
                # you skip the next day and go to the day after
                profit = max( prices[index] + helper(index+2,1), helper(index+1,0))
               
            cache[key] = profit
            return cache[key]
        
        return helper(0,1)
