# 1245. Tree Diameter
# This is a therom:
# Start at any node A and traverse the tree to find the furthest node from it, let's call it B.
# Having found the furthest node B, traverse the tree from B to find the furthest node from it, lets call it C.
# The distance between B and C is the tree diameter.
# https://codeforces.com/blog/entry/60440


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not len(edges):
            return 0
        
        adjList = defaultdict(list)
        for s,d in edges:
            adjList[s].append(d)
            adjList[d].append(s)
        
        n = len(adjList)
        def bfs(startNode):
            
            distances = [-1 for _ in range(n)]
            q = [(startNode,0)]
            visited = set()
            while q:
                length = len(q)
                for _ in range(length):
                    node, distance = q.pop(0)
                    visited.add(node)
                    distances[node] = distance
                    for nei in adjList[node]:
                        if nei not in visited:
                            q.append([nei,distance+1])
            
            return distances
        
        distances = bfs(0)
        
        maxDistance = 0
        farthestNode = -1
        for i in range(n):
            if distances[i] > maxDistance:
                farthestNode = i
                maxDistance = distances[i] 
        
        distances = bfs(farthestNode)
        return max(distances)
                
        
                    
                    
            
        
        
        
        