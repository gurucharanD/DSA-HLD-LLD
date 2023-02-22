# the minimum number of rooms needed is the 
# maximum number of rooms needed at any point
# of time between the start of the first meeting
# and end of the last meeting due to overlap

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        ans = 0
        count = 0
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        i = j = 0
        
        while i < len(intervals) and j < len(intervals):
            # if there is a meeting that is starting before
            # a meeting is ending then we need a new meeting room
            # hence we increment the counter of the meeting room
            if start[i] < end[j]:
                i+=1
                count+=1
            else:
                j+=1
                count-=1
            
            ans = max(ans,count)
        
        return ans
            