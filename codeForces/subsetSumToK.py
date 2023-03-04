from functools import lru_cache

def subsetSumToK(n, k, arr):

    @lru_cache(None)
    def helper(idx,target):

        if target == 0:
            return True
        
        if idx == 0:
            if arr[idx] == target:
                return True
            else:
                return False

        notTake = helper(idx-1,target)
        take = False
        if target >= arr[idx]:
            take = helper(idx-1,target-arr[idx])
        
        return take or notTake
    
    return helper(n-1,k)


def subsetSumToK(n, k, arr):

    dp = [[-1]*(k+1) for _ in range(n)]

    def helper(idx,target):

        if target == 0:
            return True
        
        if idx == 0:
            if arr[idx] == target:
                return True
            else:
                return False

        if dp[idx][target] != -1:
            return dp[idx][target]
            
        notTake = helper(idx-1,target)
        take = False
        if target >= arr[idx]:
            take = helper(idx-1,target-arr[idx])
        
        dp[idx][target] = take or notTake
        return dp[idx][target]
    
    return helper(n-1,k)


def subsetSumToK(n, k, arr):

    # x axis represents the target
    # y axis represents the indices
    dp = [[False]*(k+1) for _ in range(n)]
    
    # at any index of arr a target of 0 is possible
    for i in range(n):
        dp[i][0] = True
    
    # at index 0 only sum possible is arr[0] and 0
    # we check if arr[0] <= target because
    # we only target no of columns in our dp table
    if arr[0] <= k:
        dp[0][arr[0]] = True

    
    for idx in range(1,n):
        for target in range(1,k+1):

            notTake = dp[idx-1][target]
            take = False
            if target >= arr[idx]:
                take = dp[idx-1][target-arr[idx]]
            
            dp[idx][target] = notTake or take
    
    return dp[n-1][k]

def subsetSumToK(n, k, arr):

    prev = [False]*(k+1) 
    prev[0] = True
    
    if arr[0] <= k:
        prev[arr[0]] = True

    for idx in range(1,n):
        curr = [False]*(k+1)
        curr[0] = True
        for target in range(1,k+1):

            notTake = prev[target]
            take = False
            if target >= arr[idx]:
                take = prev[target-arr[idx]]
            
            curr[target] = notTake or take
        prev = curr
    
    return prev[k]



# to counter 0's in the array   

# if index == 0:

#     if target == 0 and nums[0] == 0:
#         return 2
#     elif target == nums[0] :
#         return 1
#     else:
#         return 0

# if nums[0] == 0:
#     dp[0][0] = 2
# else:
#     dp[0][0] = 1

# if nums[0]!=0 and nums[0] <= k:
#     dp[nums[0]] = 1