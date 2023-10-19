# 875. Koko Eating Bananas

# koko can decide to eat one banana from the pile
# which becomes the lower point
# the max that koko can eat in one hour is the max(piles)
# because koko chooses only one pile per hour and can eat
# all of it or k of it

# time : O(log(max(p)).len(p))
# space : O(1)

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)
        res = max(piles)

        # if koko decides to eat cap banas each hour from the pile
        # then it takes ceil(piles[i]/cap) to finish eating each pile

        def is_valid(cap):
            time = 0
            for p in piles:
                time += math.ceil(p/cap)
            
            return time <= h
        
        while low <= high:
            mid = (low+high)//2
            if is_valid(mid):
                res = min(res,mid)
                high = mid-1
            else:
                low = mid+1
        
        return res