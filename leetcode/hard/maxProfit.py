# 123. Best Time to Buy and Sell Stock III
# here you can only perform 2 transactions
# 1 transaction consists of buy and a sell
# the transaction is complete only when you sell the stock that
# you purchased previously

# This will work for K transactions as well

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