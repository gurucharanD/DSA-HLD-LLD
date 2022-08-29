# convert the given graph into a MST using prims algo
# and return the sum of the edges that are choosen
# if some of the nodes are not reachable
# then their distance would be inf in that case return -1

# this is prims algorithm
from heapq import heappush,heappop,heapify

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        n += 1
        adjList = [ []for _ in range(n+1) ]
        
        for s,d,c in connections:
            adjList[s].append([d,c])
            adjList[d].append([s,c])

        
        key = [float("inf") for _ in range(n)]
        mst = [False for _ in range(n)]
        parent = [-1 for _ in range(n)]
        
        pq = []
        heapify(pq)
        
        key[1] = 0
        heappush(pq,(0,1))
        
        while len(pq):
            dis,node = heappop(pq)
            mst[node] = True
            for nei,wei in adjList[node]:
                if key[nei] > wei and not mst[nei]:
                    key[nei] = wei
                    heappush(pq,(key[nei],nei))
                    parent[nei] = node

        total = 0
        for i in range(1,len(key)):
            if key[i] == float("inf"):
                return -1
            total+=key[i]
        
        return total
            
# kruskal's algorithm

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        n+=1
        connections.sort(key = lambda x: x[2])
        parent = [_ for _ in range(n)]
        rank = [1 for _ in range(n)]
        
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return node
        
        def union(a,b):
            par1 = find(a)
            par2 = find(b)
            
            if par1 == par2:
                return
            
            if rank[par1] < rank[par2]:
                parent[par1] = par2
                rank[par2]+=rank[par1]
            else:
                parent[par2] = par1
                rank[par1]+=rank[par2]
            
            return
        
        
        total = 0
        cost = 0
        for s,d,w in connections:
            
            parS = find(s)
            parD = find(d)
            if parS != parD:
                union(s,d)
                cost+=w
                # count the no of edges added
                total+=1

        # if no of edges added == no of nodes -1
        # checking n-2 since we did n+1 at the begining
        if total == n-2:
            return cost
        
        return -1
        
        
        
        
        

        
        