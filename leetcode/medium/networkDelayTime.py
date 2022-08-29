# appply dijkstras and return the value of the 
# distance from source to the farthest node
# O((v+e)log(v+e))

from heapq import heapify,heappush,heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = [ [] for _ in range(n+1)]
        
        for s,d,w in times:
            adjList[s].append([d,w])
        
        distance = [float("inf") for _ in range(n+1)]
        distance[k] = 0
        distance[0] = -1
        
        pq = []
        heapify(pq)
        heappush(pq,(0,(0,k)))
        
        while len(pq):
            dist,node = heappop(pq)[1]
            for nei,wei in adjList[node]:
                if distance[nei] > distance[node]+wei:
                    distance[nei] = distance[node]+wei
                    heappush( pq, (distance[nei],(distance[nei],nei)) )
        
        for i in range(1,len(distance)):
            if distance[i] == float("inf"):
                return -1
            
        return max(distance)
            