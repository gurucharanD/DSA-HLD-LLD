from heapq import heapify, heappush, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         bucket sort
#         each index is going to store a bucket, 
#         each index i, stores an array of elements that occur i times

#         buckets = [[] for _ in range(len(nums)+1)]
#         counter = Counter(nums)
        
#         for key in counter:
#             buckets[counter[key]].append(key)
            
#         ans = []
#         for bucket in reversed(buckets):
#             for j in bucket:
#                 ans.append(j)
#                 if len(ans) == k:
#                     return ans



#       max heap
        # counter = Counter(nums)
        # max_heap = [(-counter[key],key) for key in counter]
        # heapify(max_heap)
        # ans = []
        # for _ in range(k):
        #     ans.append(heappop(max_heap)[1])
        # return ans
        
# min heap
        
        counter = Counter(nums)
        pairs = [(counter[key],key) for key in counter]
        
        min_pair = min(pairs,key = lambda x:x[0])
        min_heap = [min_pair]
        heapify(min_heap)
        
        for i in range(0,len(pairs)):
            val,key = pairs[i]
            
            if val >= min_heap[0][0]:
                heappush(min_heap,(val,key))
            
            if len(min_heap) > k:
                heappop(min_heap)
                
        ans = []
        for _ in range(k):
            ans.append(heappop(min_heap)[1])
        return ans


        
        
        
        

    