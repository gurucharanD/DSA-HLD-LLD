# if a graph can be colored using two colors
# then the graph can be called a bipartite graph

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
            
        n = len(graph)
        colors = [-1 for _ in range(n)]
        
        def bfs(node):
            colors[node] = 1
            q = [node]
            while len(q):
                currNode = q.pop(0)
                newColor = 1 if colors[currNode] == 0 else 0
                for nei in graph[currNode]:
                    if colors[nei] == -1:
                        colors[nei] = newColor
                        q.append(nei)
                    elif colors[nei] == colors[currNode]:
                        return False
            
            return True
            
        print(colors)
        for i in range(n):
            if colors[i] == -1:
                if not bfs(i):
                    return False
                
        print(colors)
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
            
        n = len(graph)
        colors = [-1 for _ in range(n)]
        
        def isValid(node,color):
            for nei in graph[node]:
                if colors[nei] == color:
                    return False
            return True
        
        def dfs(node,color):
            
            if not isValid(node,color):
                return False
            
            colors[node] = color
            newColor = 1 if color == 0 else 0
            
            for nei in graph[node]:
                if colors[nei] == -1:
                    res = dfs(nei,newColor)
                    if not res:
                        return False
                elif colors[nei] == color:
                    return False
            
            return True
            
        for i in range(n):
            if colors[i] == -1:
                if not dfs(i,0):
                    return False
                
        return True