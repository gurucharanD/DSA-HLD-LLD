# positive weights
# directed edges
# self loops 

# consider or clarify these above questions 
# before you proceed with the solution
# as they result in edge cases

# bfs with min heap
# every time you find a new min distance
# insert the node and new min distance into the heap

from heapq import heappop, heappush, heapify

def dijkstrasAlgorithm(start, edges):
    n = len(edges)
    pq = []
    heapify(pq)
    heappush(pq,(0,start))
    distance = [float("inf") for _ in range(n)]
    distance[start] = 0

    while pq:

        distanceTraveled,currNode = heappop(pq)
        for nei,wei in edges[currNode]:

            if distance[nei] > distanceTraveled+wei:
                distance[nei] = distanceTraveled+wei
                heappush(pq,(distanceTraveled+wei,nei))

    for i in range(0,len(distance)):
        distance[i] = -1 if distance[i] == float("inf") else distance[i]
    return distance

def dijkstra(self, V, adj, S):
        
        q = [(0,S)]
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0
        
        while q:
            
            distTraveled,node = heappop(q)
            for nei,wei in adj[node]:
                if dist[nei] > distTraveled+wei:
                    dist[nei] = distTraveled+wei
                    heappush(q,(dist[nei],nei))
        
        for idx,val in enumerate(dist):
            if val == float("inf"):
                dist[idx] = -1
        
        return dist
    
