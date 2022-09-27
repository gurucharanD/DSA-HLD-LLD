# build parent relations for each variable
# considering each variable as a node when the 
# symbol check is ==

# a == b implies a <- b
# b == c implies b <- c, since b's parent is already c
# we can do a path reduction and make a as the parent for both 
# b and c 
#    a
#  /   \
# b     c
# if there is a equation c != a
# we find parent c and parent a 
# whihc implies a != a, which is False
# therefore, the given set of equations are not satisfiable

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = [_ for _ in range(26)]
        
        def union(a,b):
            parA = find(a)
            parB = find(b)
            parent[parB] = parA
            return
        
        def find(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v
        
        for eqn in equations:
            
            if eqn[1] == '=':
                a = ord(eqn[0]) - ord('a')
                b = ord(eqn[3]) - ord('a')
                
                union(a,b)
                
        for eqn in equations:
            
            if eqn[1] == '!':
                a = ord(eqn[0]) - ord('a')
                b = ord(eqn[3]) - ord('a')
                
                if find(a) == find(b):
                    return False
        
        return True
        
        
                
        
        
        

        