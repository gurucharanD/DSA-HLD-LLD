class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
                
        n = len(coins)
        
        dp = [[float("inf")]*(amount+1) for _ in range(n)]
        
        for tar in range(amount+1):
            if tar % coins[0] == 0:
                dp[0][tar] = tar // coins[0]
        
        for idx in range(1,n):
            for tar in range(0,amount+1):
                ans = dp[idx-1][tar]
                if coins[idx] <= tar:
                    ans = min(ans,1+dp[idx][tar-coins[idx]])

                dp[idx][tar] = ans
        
        
        sol = dp[n-1][amount]
        if sol == float("inf"):
            return -1
        
        return sol


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
                
        n = len(coins)
        
        prev = curr = [float("inf")]*(amount+1)
        
        for tar in range(amount+1):
            if tar % coins[0] == 0:
                prev[tar] = tar // coins[0]
        
        for idx in range(1,n):
            for tar in range(0,amount+1):
                ans = prev[tar]
                if coins[idx] <= tar:
                    ans = min(ans,1+curr[tar-coins[idx]])

                curr[tar] = ans
        
        
        sol = prev[amount]
        if sol == float("inf"):
            return -1
        
        return sol
                
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
            
            
            