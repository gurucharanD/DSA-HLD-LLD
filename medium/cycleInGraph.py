# Do a DFS at each node
# when you are not sure about what to do 
# in the case of a graphs problem
# we just run the traversal algorithms

def cycleInGraph(edges):
	
	numberOfNodes = len(edges)
	
	visited = [ False for _ in range(numberOfNodes)]
	currentlyInStack = [False for _ in range(numberOfNodes)]
	
	for node in range(numberOfNodes):
		if visited[node]:
			continue
			
		containsCycle = isNodeInCycle(edges,node,visited,currentlyInStack)
		if containsCycle:
			return True
		
	return False


def isNodeInCycle(edges,node,visited,currentlyInStack):
	visited[node] = True
	currentlyInStack[node] = True
	neighbours = edges[node]
	
	for neighbour in neighbours:
		if not visited[neighbour]:
			containsCycle = isNodeInCycle(edges,neighbour,visited,currentlyInStack)
			if containsCycle:
				return True
		elif currentlyInStack[neighbour]:
			return True
		
	currentlyInStack[node] = False
	return False

