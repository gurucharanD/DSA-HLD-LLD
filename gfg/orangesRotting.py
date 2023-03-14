# since all the rotten oranges are rotting its neighbor cells at the same time
# Q all the rotten oranges at once and Deque them all at once
# for this use the level order traversal technique
# traverse the grid using BFS untill all the rotten oranges are traversed
# or all the fresh oranges are rotten
# after traversing each batch of rotten oranges increment the time
# after a fresh orange is marked as rotten, reduce the count of the fresh orange by 1
 
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		fresh = 0
		time = 0
		q = []
		rows = len(grid)
		cols = len(grid[0])
		
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1

        while q and fresh:
            currRot = len(q)
            for _ in range(currRot):
                i,j = q.pop(0)
                for r,c in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_i = i+r
                    new_j = j+c
                    if new_i < 0 or new_j<0 or new_i >= rows or new_j >= cols:
                        continue
                    if grid[new_i][new_j] != 1:
                        continue
                    grid[new_i][new_j] = 2
                    q.append([new_i,new_j])
                    fresh-=1

                    time+=1

        if fresh != 0:
            return -1

        return time
		            
		            
		
		
		


#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends