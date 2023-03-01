# https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0
from typing import *
from functools import lru_cache
  
from typing import *
from functools import lru_cache

# memoization   
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    rows = n
    cols = 3

    dp = [[-1]*4 for _ in range(n)]

    def helper(day,last):
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi,points[0][i])
            return maxi
        
        if dp[day][last] != -1:
            return dp[day][last]
        
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi,points[day][i]+helper(day-1,i))
        dp[day][last] = maxi
        return maxi
    
    return helper(n-1,3)

# tabulation
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    rows = n
    cols = 3

    dp = [[-1]*4 for _ in range(n)]

   
    dp[0][0] = max(points[0][1],points[0][2])
    dp[0][1] = max(points[0][0],points[0][2])
    dp[0][2] = max(points[0][0],points[0][1])
    dp[0][3] = max(points[0][0],points[0][1],points[0][2])

    # print(dp[0])

    for day in range(1,n):
        for last in range(0,4):
            for task in range(0,3):
                if task != last:
                    dp[day][last] = max(dp[day][last],points[day][task]+dp[day-1][task])
    
    for d in dp:
        print(d)
    return dp[n-1][3]

print(ninjaTraining(3,
[
    [1, 2, 5 ],
    [3, 1, 1],
    [3, 3 ,3]
]
))

print(ninjaTraining(3,
[
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]
))

print(ninjaTraining(2,
[
    [10, 50, 1],
    [5, 100, 11]
]
))

print(ninjaTraining(3,
[
    [18, 11, 19],
    [4, 13, 7],
    [1, 8, 13]
]
))

