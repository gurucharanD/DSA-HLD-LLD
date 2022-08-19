N = 4
m = [[1, 0, 0, 0],[1, 1, 0, 1], [1, 1, 0, 0],[0, 1, 1, 1]]
# N = 2
# m = [[1, 0],[1, 0]]
         
visited = [ [0 for _ in range(0,N)] for _ in range(0,N)]
ans = []
def helper(row,col,path,visited):
    # print(row,col,path)


    if row < 0 or col < 0: return
    if row >= N or col >= N : return 
    if visited[row][col] == 1 or m[row][col] == 0: return
    if row == N-1 and col == N-1:
        print("here")
        ans.append(path)
        return

    visited[row][col] = 1
    helper(row+1,col,path+"D",visited)
    visited[row][col] = 0
    
    visited[row][col] = 1
    helper(row-1,col,path+"U",visited)
    visited[row][col] = 0
    
    visited[row][col] = 1
    helper(row,col-1,path+"L",visited)
    visited[row][col] = 0
    
    visited[row][col] = 1
    helper(row,col+1,path+"R",visited)
    visited[row][col] = 0
    
    return

helper(0,0,"",visited)
print(ans)