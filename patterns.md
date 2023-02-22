
Instead of learning solutions of LeetCode questions, understand patterns! 🙂

For ex.

If input array is sorted then
- Binary search
- Two pointers

If asked for all permutations/subsets then
- Backtracking

If given a tree then
- DFS
- BFS

If given a graph then
- DFS
- BFS

If given a linked list then
- Two pointers

If recursion is banned then
- Stack

If must solve in-place then
- Swap corresponding values
- Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then
- Dynamic programming

If asked for top/least K items then
- Heap

If asked for common strings then
- Map
- Trie

Else
- Map/Set for O(1) time & O(n) space
- Sort input for O(nlogn) time and O(1) space

- if there are references to neighbourhood,use two pass approach

___________________________________

Inplace operation on array Template:

l points to the index of elements that
you want to move to the end of the array
r points to the index of elements that 
you want to move to the beginnig of the array

        l = 0
        r = 0
        for r in range(len(nums)):
            if nums[r]!=val:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        
        return l
___________________________________

pattern: marking the value at nums[index] to negative

# update the numbers at nums[index] to negative
# after updating all the numbers in the array
# the indexes which still have the positive numbers 
# are the values that are missing form the input array
# this approach works only because the input array is
# in the range of 1 to len(nums)

___________________________________