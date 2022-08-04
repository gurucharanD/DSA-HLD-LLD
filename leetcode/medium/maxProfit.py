# every day you will have two options
# you can buy or sell
# if you can only sell after you buy the stock

# you can still decide to not to sell the stock
# even if you are allowed to sell the stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        cache = {}        
        def helper(index,buy):
            
            key = "{}-{}".format(index,buy)
            if key in cache:
                return cache[key]
            
            if index == len(prices):
                return 0
                         
            profit = 0
            if buy:
                # since you are buying profit is negative
                # since you made the purchase you need to sell the next day
                # you decide not to buy on current day, you can buy on the next day
                profit = max( -prices[index] + helper(index+1,0), helper(index+1,1))
            else:
                profit = max( prices[index] + helper(index+1,1), helper(index+1,0))
               
            cache[key] = profit
            return cache[key]
        
        return helper(0,1)



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [[0,0] for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0

        for index in range(n-1,-1,-1):
            for buy in [0,1]:
                
                if buy:
                    dp[index][buy] = max( -prices[index] + dp[index+1][0],dp[index+1][1])
                else:
                    dp[index][buy] = max( prices[index] + dp[index+1][1],dp[index+1][0] )
        
            
        return dp[0][1]


# 188. Best Time to Buy and Sell Stock IV

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        def helper(index,buy,cap):
            
            key = "{}-{}-{}".format(index,buy,cap)
            if key in cache:
                return cache[key]
            
            if index == len(prices) or cap == 0:
                return 0
            
            if buy:
                cache[key] = max(
                    -prices[index]+helper(index+1,0,cap),
                    helper(index+1,1,cap)
                )
            else:
                cache[key]= max(
                    prices[index]+helper(index+1,1,cap-1),
                    helper(index+1,0,cap)
                )
            return cache[key]
        
        return helper(0,1,2)
                                         
        
                