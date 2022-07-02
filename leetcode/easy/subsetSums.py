# if you pass the subset and perform a sum of the subset 
# in the base case, this makes the time complexity O(2^N * N)
# to avoid the extra N, you can track the sum at each step
# by including or not including the element at the current index
# into the subset, on base case append the sum into the result array

def subsetSums(arr):
    subsets = []
    def helper(index,currSum):
        if index >= len(arr):
            subsets.append(currSum)
            return
            
        helper(index+1,currSum)
        # subset.append(arr[index])
        helper(index+1,currSum+arr[index])
        # subset.pop()

    helper(0,0)
    return subsets
    
print(subsetSums([1,2,3]))