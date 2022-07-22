# https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0

from typing import *
 
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    def helper(r,c):
        if r >= len(points) or c >= len(points[0]):
            return 0
        sol = 0
        for i in range(r,len(points)):
            for j in range(0,len(points[0])):
                if j != c:
                    sol = max(
                        sol,
                        points[i][j] + helper(i+1,j)
                    )
        return sol
    
    return helper(0,0)



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

