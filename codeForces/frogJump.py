# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0

from typing import *

def frogJump(n: int, heights: List[int]) -> int:
    
    dp = [0 for _ in heights]
    dp[1] = abs(dp[1]-dp[0])
    
    for i in range(2,len(heights)):
        dp[i] = min((heights[i]-heights[i-1])+dp[i-1],(heights[i]-heights[i-2])+dp[i-2])
        
    return dp[-1]
    

def helper(i):
if i == 0:
    return 0
if i == 1:
    return abs(heights[1]-heights[0])

return min(abs(heights[i]-heights[i-1])+helper(i-1),abs(heights[i]-heights[i-2])+helper(i-2))
