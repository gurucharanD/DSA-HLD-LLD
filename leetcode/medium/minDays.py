# standard Binary search Template


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # check if m boquets can be created on the passed day
        def feasible(days) -> bool:
            flowers=bouquet=0                
            for d in bloomDay:
                # if k continuous flowers bloom
                # by the passed day, create a boquet
                if d>days: 
                    flowers=0
                else:
                    flowers+=1

                    if flowers==k:
                        bouquet+=1
                        flowers=0
                
            return bouquet>=m

        if len(bloomDay) < m * k:
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
