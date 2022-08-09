# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        merged = [intervals[0]]
        
        start = 0
        end = 1
        for i in range(1,len(intervals)):
            currentInterval = intervals[i]
            lastInterval = merged[-1]
            
            if currentInterval[start] <= lastInterval[end]:
                lastInterval[end] = max(lastInterval[end],currentInterval[end])
            else:
                merged.append(currentInterval)
                
            
        return merged
            
            
        