# 1376. Time Needed to Inform All Employees
# create a hashmap of the managers and their reportees
# where maanger is the key and reportees are the values
# and start at the headId and do a BFS, adding the 
# reportees of the manger into the Queue everytime

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hashMap = {}
        for i in range(0,len(manager)):
            if manager[i] in hashMap:
                hashMap[manager[i]].append(i)
            else:
                hashMap[manager[i]]=[i]
                    
        
        time = [0]*len(manager)
        time[headID] = informTime[headID]
        
        queue = [headID]
        
        while len(queue) != 0:
            node = queue.pop(0)
            if headID != node:
                time[node] = informTime[node] + time[manager[node]]
                
            if node in hashMap:
                queue = queue + hashMap[node]

        return max(time)