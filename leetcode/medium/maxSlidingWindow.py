# use a deque, and store the indices of the array inside this
# this deque will store the monotonic decreasing queue

# as long as the element at current index is greater than the 
# element at the top index of the deque in the array
# keep poping the elements from the deque

# once you find an index that points to an element greater than
# or equal to the element at the current index then we append the
# current index to the deque

# if the window size is atleast k then 
# we can keep adding element at the index 0 of deque
# in the nums array to the ans

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # dq only stores the indices of the elements
        # the dq will be monotonic decreasing queue
        
        ans = []
        dq = deque([])
        n = len(nums)

        for i in range(0,n):
            # remove the indices in the dq 
            # which will be out of bound for the current window
            # if the current index is 4 and k is 3
            # the window under consideration should be
            # from 2 to 4, hence if the dq has indexes less
            # than 2 stored inside it, pop them
            if dq and dq[0] <= i-k:
                dq.popleft()
            
            # keep poping the indices from the dq until
            # the element at the index at the top of the dq
            # is less than the element at current index
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            # if the size of the window is
            # atleast k then we have an answer
            # for the current window at the index 0
            # of the dq
            if dq and i >= k-1:
                ans.append(nums[dq[0]])
        
        return ans

