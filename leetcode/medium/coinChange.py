class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [ float("inf") for _ in range(amount+1)]
        dp[0] = 0
        
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min( dp[i], 1+dp[i-coin] )
        
        return dp[len(dp)-1] if dp[len(dp)-1] != float("inf") else -1

# in the base case, you cant return 0 because since we are 
# considering the minimum number of coins if you return a 0
# 0 will always be considered as the minimum coins

# you should avoid going beyond zero to avoid extra recursion calls
# if you reach index 0 and you coin at 0 divided by target gives 0
# return target / coin
# example :
#     coin 1 is at index 0 and your target is 2
#     you need two coins to make 2 with 1 coin
#     this will help avoid few recursion calls

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
                
        cache ={}
        
        def helper(index,target):
            key = "{}-{}".format(index,target)
            
            if key in cache:
                return cache[key]
            
            if index == 0:
                if target%coins[index] == 0:
                    return target//coins[index]
                else:
                    return float("inf")

            
            ans = helper(index-1,target)
            if coins[index] <= target:
                ans = min(ans,1+helper(index,target-coins[index]))
            
            cache[key] = ans
            return ans
        
        sol = helper(len(coins)-1,amount)
        if sol == float("inf"):
            return -1
        
        return sol
            
            
            