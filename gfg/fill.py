# start at the cells on the boundary 
# that have a value of O and visit the neighbours 
# of these cells if they also have a O using BFS
# after BFS if there are cells that have O and are not visited
# then that cell is enclosed by X on all sides
# so convert it into a X

# Replace O's with X's
#  multisource BFS

class Solution:
    def fill(self, n, m, mat):
        
        rows = len(mat)
        cols = len(mat[0])
        visited = set()
        q = []
        # first row
        for i in range(0,cols):
            if mat[0][i] == 'O':
                q.append((0,i))
        
        # last row
        for i in range(0,cols):
            if mat[-1][i] == 'O':
                q.append((rows-1,i))

        # first col
        for i in range(1,rows-1):
            if mat[i][0] == 'O':
                q.append((i,0))
            
        # last col
        for i in range(1,rows-1):
            if mat[i][-1] == 'O':
                q.append((i,cols-1))
                
        
        while q:
            r,c = q.pop(0)
            visited.add((r,c))
            for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_r = r+i
                new_c = c+j
                if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                    continue
                if (new_r,new_c) in visited:
                    continue
                
                if mat[new_r][new_c] == 'O':
                    q.append((new_r,new_c))
                    
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 'O' and (i,j) not in visited:
                    mat[i][j] = 'X'
        
        return mat
        
        
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends