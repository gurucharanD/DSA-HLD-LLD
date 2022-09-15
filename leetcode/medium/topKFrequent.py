from heapq import heappop, heappush, heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         bucket sort
#         we take an array bcs if 2 numbers appear same number of times
# we should be able to save both of them to the array      
        buckets = [ [] for _ in range(0,len(nums)+1)]
        counter = Counter(nums)
        
        # [1,1,1,2,2,3]
        # find the no of times each number appeared in nums
        # [[], [3], [2], [1], [], [], []]

        for count in counter:
            buckets[counter[count]].append(count)
            
        index = len(nums)
        ans = []
        
        for i in range(len(buckets)-1,0,-1):
            
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        
        
        