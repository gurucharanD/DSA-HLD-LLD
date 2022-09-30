# 1129. Shortest Path with Alternating Colors
# level order BFS
# we do level order BFS because we want to start the BFS
# using blue edges and red edges at the same time

# you can visit the same node again but using a different
# colored edge
# example: 
# 5 nodes
# red -> [[0,1],[1,2],[2,3],[3,4]]
# blue -> [[1,2],[2,3],[3,1]]
# ans -> [0,1,2,3,7]

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        distances = [-1 for _ in range(n)]
        adjList = {}
        adjList[1] = defaultdict(list)
        adjList[-1] = defaultdict(list)

            
        for s,d in redEdges:
            adjList[1][s].append((d,1))
        for s,d in blueEdges:
            adjList[-1][s].append((d,-1))
            
        q = [[0,-1,0],[0,1,0]]
        visited = set()
        
        while q:
            length = len(q)
            for _ in range(length):
                node,color,distance = q.pop(0)
                
                if distances[node] == -1:
                    distances[node] = distance
                visited.add((node,color))
                
                for nei,_ in adjList[-color][node]:
                    if (nei,-color) not in visited:
                        q.append([nei,-color,distance+1])
                        
        return distances
                
            
            
            

        
        
            