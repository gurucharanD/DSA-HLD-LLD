from functools import lru_cache

prices = [3,3,5,0,0,3,1,4]
n = len(prices)

@lru_cache(None)
def helper(i,j,k):
    if i == n or k == 0:    
        return 0
    
    p = 0
    if j:
        p = max(-prices[i]+ helper(i+1,0,k),helper(i+1,1,k))
    else:
        p = max(prices[i]+ helper(i+1,1,k),helper(i+1,0,k))
    
    return p

helper(0,1,2)