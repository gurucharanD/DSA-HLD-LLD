#Number Of Enclaves
# multisource BFS
# always use Deque for BFS
from typing import List
from collections import deque

class Solution:    
    def numberOfEnclaves(self, mat: List[List[int]]) -> int:
        # code here
        rows = len(mat)
        cols = len(mat[0])
        visited = set()
        q = deque([])
        # first row
        for i in range(0,cols):
            if mat[0][i] == 1:
                q.append((0,i))
        
        # last row
        for i in range(0,cols):
            if mat[-1][i] == 1:
                q.append((rows-1,i))

        # first col
        for i in range(1,rows-1):
            if mat[i][0] == 1:
                q.append((i,0))
            
        # last col
        for i in range(1,rows-1):
            if mat[i][-1] == 1:
                q.append((i,cols-1))
                
        
        while q:
            r,c = q.popleft()
            visited.add((r,c))
            for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_r = r+i
                new_c = c+j
                if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                    continue
                if (new_r,new_c) in visited:
                    continue
                
                if mat[new_r][new_c] == 1:
                    q.append((new_r,new_c))
        
        ans = 0
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if mat[i][j] == 1 and (i,j) not in visited:
                    ans+=1
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends