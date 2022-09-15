from heapq import heappop, heappush, heapify

def dijkstrasAlgorithm(start, edges):
    n = len(edges)
    pq = []
    heapify(pq)
    heappush(pq,(0,(start,0)))
    distance = [float("inf") for _ in range(n)]
    distance[start] = 0

    while len(pq):

        currNode,distanceTraveled = heappop(pq)[1]
        for nei,wei in edges[currNode]:

            if distance[nei] > distanceTraveled+wei:
                distance[nei] = distanceTraveled+wei
                heappush(pq,(distanceTraveled+wei,(nei,distanceTraveled+wei)))

    for i in range(0,len(distance)):
        distance[i] = -1 if distance[i] == float("inf") else distance[i]
    return distance
        
    
