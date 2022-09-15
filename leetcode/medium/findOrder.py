class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if numCourses == 1:
            return [0]
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        
        adjList = [ [] for _ in range(numCourses)]
        visited = [ False for _ in range(numCourses)]
        currentlyInStack = [False for _ in range(numCourses)]
        order = []

        for d,s in prerequisites:
            adjList[s].append(d)
        

        def isNodeInCycle(edges,node,visited,currentlyInStack,order):
            visited[node] = True
            currentlyInStack[node] = True
            neighbours = edges[node]

            for neighbour in neighbours:
                if not visited[neighbour]:
                    if isNodeInCycle(edges,neighbour,visited,currentlyInStack,order):
                        return True
                elif currentlyInStack[neighbour]:
                    return True
                    
            # topological sort
            order.append(node)
            currentlyInStack[node] = False
            return False
        
        for node in range(numCourses):
            if visited[node]:
                continue

            containsCycle = isNodeInCycle(adjList,node,visited,currentlyInStack,order)
            if containsCycle:
                return []

        return order[::-1]
        