# 547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        edges = []
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    edges.append([i,j])
                    
        def countComponents(n,edges):

                parent = [_ for _ in range(n)]
                rank = [1] * n

                def find(v):

                    while parent[v] != v:
                        parent[v] = parent[parent[v]]
                        v = parent[v]
                    return v

                def union(a,b):
                    p1 = find(a)
                    p2 = find(b)

                    if p1 == p2:
                        return 0

                    if rank[p2] > rank[p1]:
                        parent[p1] = p2
                        rank[p2]+=rank[p1]
                    else:
                        parent[p2] = p1
                        rank[p1]+=rank[p2]

                    return 1

                res = n
                for n1,n2 in edges:
                    res -= union(n1,n2)

                return res
            
        
        return countComponents(n,edges)
        