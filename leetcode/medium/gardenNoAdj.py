# construct an adjacency list for all nodes
# and check if all the nodes can be colored with 4 colors
# if the nodes doesnt have any adjacent nodes fill it with 1
#  


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        if len(paths) == 0:
            return [1]*n
        
        M = 4
        adjList = {}
        for edge in paths:
            if edge[0] in adjList:
                adjList[edge[0]].append(edge[1])
            else:
                adjList[edge[0]] = [edge[1]]

            if edge[1] in adjList:
                adjList[edge[1]].append(edge[0])
            else:
                adjList[edge[1]] = [edge[0]]
                
        def isValidColor(node,color,takenColors):
            neighbours = adjList[node]
            for neighbour in neighbours:
                if neighbour in takenColors and takenColors[neighbour] == color:
                    return False
            return True
        
        def helper(node,takenColors):
            if node == n+1:
                return True
            if node not in adjList:
                takenColors[node] = 1
                return helper(node+1,takenColors)

            for i in range(1,M+1):
                if isValidColor(node,i,takenColors):
                    takenColors[node] = i
                    return helper(node+1,takenColors)
                    
            return False

        colors = {}
        helper(1,colors)
        return colors.values()
        