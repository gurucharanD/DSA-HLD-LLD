# 121. Best Time to Buy and Sell Stock
# initially you purchase the stock on day 0
# and keep iterating over given prices to sell on a day with higher price
# if price is high, you sell and calculate the profit
# else you buy on that day and keep checking for another day with higher price


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        buy = 0
        
        for sell in range(1,len(prices)):
            
            if prices[sell] > prices[buy]:
                profit = max(profit,prices[sell]-prices[buy])
            else:
                buy = sell
                
        return profit
        