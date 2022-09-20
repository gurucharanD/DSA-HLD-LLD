# 207. Course Schedule


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        adjList = defaultdict(list)
        visited = [ False for _ in range(numCourses)]
        currentlyInStack = [False for _ in range(numCourses)]

        for d,s in prerequisites:
            adjList[s].append(d)
        

        def isNodeInCycle(edges,node,visited,currentlyInStack):
            visited[node] = True
            currentlyInStack[node] = True
            neighbours = edges[node]

            for neighbour in neighbours:
                if not visited[neighbour]:
                    if isNodeInCycle(edges,neighbour,visited,currentlyInStack):
                        return True
                elif currentlyInStack[neighbour]:
                    return True
            
            currentlyInStack[node] = False
            return False
        
        for node in range(numCourses):
            # if node is visited, then a dfs
            # has already been done through that node
            # so, we dont have to do another cycle check
            if visited[node]:
                continue

            if isNodeInCycle(adjList,node,visited,currentlyInStack):
                return False
            
        return True
