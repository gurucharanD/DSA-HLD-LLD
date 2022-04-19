# treat the input matrix as a graph and each 
# element in the input array as node which has a value
# and neighbouring nodes

# whenever you encounter a node that has a value
# you can apply BFS or DFS to the neighbouring nodes
# you stop when you encounter a 0

# keep track of all the nodes that we visited
# when you reach a node that you have already visited
# just skip it

# at every element which we consider as a node
# do the following,

# if the value of the node is 1
# increment the length of the river and mark the node as visited
# and traverse the top,left,down,right neighbours of the node

# if the value of the node is 0
# just mark the node as visited and do nothing

# time : O(width * height )
# space : O( width * height) -> auxilary matrix to save visited nodes

# as we are visiting every single node in the graph 
# and peeking at the neighbours, since the total no.of 
# neighbours is constant i.e 4 we can ignore this 

# [
#  [1, 0, 0, 1, 0],
#  [1, 0, 1, 0, 0],
#  [0, 0, 1, 0, 1], 
#  [1, 0, 1, 0, 1],
#  [1, 0, 1, 1, 0]
# ]

# [
#  [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0], 
#  [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0], 
#  [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
#  [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0], 
#  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
# ]



def riverSizes(matrix):
    # Write your code here.
	sizes = []
	visited = [[False for value in row] for row in matrix]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			
			if visited[i][j]:
				continue
			traverseNode(i,j,matrix,visited,sizes)

	return sizes

def traverseNode(i,j,matrix,visited,sizes):
	currentRiverSize = 0
	# DFS
	nodesToExplore = [[i,j]]	
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		currentRiverSize += 1
		
		unvisitedNeighbours = getUnvisted(i,j,matrix,visited)
		
		for neighbour in unvisitedNeighbours:
			nodesToExplore.append(neighbour)
			
	if currentRiverSize>0:
		sizes.append(currentRiverSize)

def getUnvisted(i,j,matrix,visited):
	unvisitedNeighbours = []
	
    # above node
	if i > 0 and not visited[i-1][j]:
		unvisitedNeighbours.append([ i-1, j ])
    # right node
	if i < len(matrix)-1 and not visited[i+1][j]:
		unvisitedNeighbours.append([ i+1, j ])
    # left node
	if j > 0 and not visited[i][j-1]:
		unvisitedNeighbours.append([ i, j-1 ])
    # right node
	if j < len(matrix[0])-1 and not visited[i][j+1]:
		unvisitedNeighbours.append([ i, j+1 ])
		
	return unvisitedNeighbours

	
	
		
		


