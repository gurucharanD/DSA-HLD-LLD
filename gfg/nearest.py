import collections
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearestnearest(self, mat):
		#Code here
        row = len(mat)
        col = len(mat[0])
        queue = collections.deque()
        visited = set()
        distance = [[0 for x in range(col)] for y in range(row)]

        direction_x = [-1, 0, 1, 0]
        direction_y = [0, 1, 0, -1]

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i,j))

        while queue:
            x, y, dis = queue.popleft()
            distance[x][y] = dis
            for d in range(4):
                xx, yy = x + direction_x[d], y + direction_y[d]
                if xx < 0 or xx == row or yy < 0 or yy == col:
                    continue
                
                if not (xx,yy) in visited:
                    queue.append((xx, yy, dis + 1))
                    visited.add((xx, yy))
        return distance
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends