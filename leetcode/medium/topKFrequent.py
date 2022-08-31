from heapq import heappop, heappush, heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         bucket sort
        buckets = [ [] for _ in range(0,len(nums)+1)]
        counter = Counter(nums)
        
        for count in counter:
            buckets[counter[count]].append(count)
            
        index = len(nums)
        ans = []
        
        for i in range(len(buckets)-1,0,-1):
            
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        
        
        