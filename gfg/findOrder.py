#User function Template for python3
# Alien Dictionary
# topological sort

from collections import defaultdict

class Solution:
    def findOrder(self,dict, N, K):
        adj = [[] for _ in range(K)]
        
        for i in range(len(dict)-1):
            currWord = dict[i]
            nextWord = dict[i+1]
            i = 0
            j = 0
            
            while i<len(currWord) and j<len(nextWord):
                if currWord[i] != nextWord[j]:
                    adj[ord(currWord[i])-ord('a')].append( 
                                  ord(nextWord[j])-ord('a')
                                )
                    break
                i+=1
                j+=1

  
        visited = [False]*K
        inSamepath = [False]*K

        topo = []
        
        def dfs(node):
            nonlocal topo
            visited[node] = True
            inSamepath[node] = True
            
            for nei in adj[node]:
                if not visited[nei]:
                    if dfs(nei):
                        return True
                elif inSamepath[nei]:
                    return True
            
            topo.append(chr(node+ord('a')))
            inSamepath[node] = False
            return False
        
        for node,lis in enumerate(adj):
            if not visited[node]:
                if dfs(node):
                    return 0
        
        ans = ''
        for char in topo[::-1]:
            ans += char
        
        return ans
            
            
                    
