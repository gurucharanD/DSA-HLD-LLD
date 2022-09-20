class Trie:
    def __init__(self):
        self.trie = {}
        
    def add(self,word):
        node = self.trie
        
        for c in word:
            if c not in node:
                node[c] = {}
            
            node = node[c]
        node["*"] = True
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = Trie()
        
        for word in words:
            root.add(word)
        
        m = len(board)
        n = len(board[0])
        
        res , visit = set(),set()
        
        def dfs(r,c,node,word):
            
            if r < 0 or c < 0 : return
            if r >= m or c >= n : return
            if board[r][c] not in node: return
            if (r,c) in visit: return
            
            visit.add((r,c))
            node = node[board[r][c]]
            word += board[r][c]
            if "*" in node:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))
            
        
        for i in range(m):
            for j in range(n):
                
                dfs(i,j,root.trie,"")
        
        return list(res)
                
        
            
            
        