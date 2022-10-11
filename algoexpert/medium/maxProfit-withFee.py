class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        cache = {}        
        def helper(index,buy):
            
            key = "{}-{}".format(index,buy)
            if key in cache:
                return cache[key]
            
            if index == len(prices):
                return 0
                         
            profit = 0
            if buy:
                profit = max( -prices[index] + helper(index+1,0), helper(index+1,1))
            else:
                # a transaction is complete only when you sell the stock
                # deduct the transaction fee everytime you sell the stock
                # you can pay the fee on buy as well, if you need to pay it only once
                profit = max( prices[index]-fee + helper(index+1,1), helper(index+1,0))
               
            cache[key] = profit
            return cache[key]
        
        return helper(0,1)