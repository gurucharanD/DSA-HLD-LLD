# whenever a subset is found
# we go back to the first index
# and start creating a new subset
# from index 0 with the elements that 
# are not taken

# if we are able to find k-1 subsets of targetsum
# then the remaining subset is also having a 
# desired sum of the target sum

# to avoid repeated work
# we use the taken elements
# to cache the results

class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
    
        total_array_sum = sum(arr)
        
        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        taken = ['0'] * n
        
        memo = {}
        
        def backtrack(index, count, curr_sum):
            n = len(arr)
            
            taken_str = ''.join(taken)
      
            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True
            
            # No need to proceed further.
            if curr_sum > target_sum:
                return False
            
            # If we have already computed the current combination.
            if taken_str in memo:
                return memo[taken_str]
            
            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]
            
            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if taken[j] == '0':
                    # Include this element in current subset.
                    taken[j] = '1'
                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
                    # Backtrack step.
                    taken[j] = '0'
                    
            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            memo[taken_str] = False
            return memo[taken_str] 
        
        return backtrack(0, 0, 0)