def canPartition(arr, n):
    # Write your code here.
    if sum(arr) % 2:
        return False
        
    k = sum(arr)//2

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