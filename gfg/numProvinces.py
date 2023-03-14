# no of provinces in a graph is equal to the no of connected components
# which is equal to the no of time dfs can be invoked starting at a node in the given graph

# convert given adj matrix into adjlist

def numProvinces(self, adj, V):
    # code here 
    adjList = {}
    for i in range(len(adj)):
        adjList[i] = []
        for j in range(len(adj[i])):
            if i != j and adj[i][j]==1:
                adjList[i].append(j)
                
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for nei in adjList[node]:
            if nei not in visited:
                dfs(nei)
                
    count = 0
    for node in adjList:
        if node not in visited:
            dfs(node)
            count+=1
    
    return count