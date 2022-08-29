# bellmon ford algorithm
# except instead of relaxing the nodes n-1 times
# we do it only for k+1 times

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        distance = [ float("inf") ]*n
        distance[src] = 0
        
        for i  in range(k+1):
            # tmp saves the distance from u to v after each iteration
            tmp = distance.copy()
            for s,d,w in flights:
                tmp[d] = min(tmp[d], distance[s]+w)
            distance = tmp.copy()
        
        if distance[dst] == float("inf"):
            return -1
    
        return distance[dst]
        
        
        