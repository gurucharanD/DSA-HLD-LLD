def findDistance(source,target,edges):
	if source == target:
		return 0

	minDistance = float("inf")
	sourceEdges = edges[source]
	for edge in sourceEdges:
		if edge[0] == target:
			minDistance = edge[1]
		minDistance = min( minDistance, edge[1] + findDistance(edge[0],target,edges) )
	return minDistance

def dijkstrasAlgorithm(start, edges):
	distances = []
	print(edges)
	for i in range(0,len(edges)):
		distance = findDistance(start,i,edges)
		if distance == float("inf"):
			distance = -1
		distances.append(distance)

	return distances
