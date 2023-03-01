from functools import lru_cache

def uniquePaths(m, n):
	# memoization

	dp = [[-1]*(n) for _ in range(m)]

	def helper(i,j,dp):
		if i == 0 and j == 0:
			return 1
		
		if i < 0 or j < 0:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]
		
		dp[i][j] = helper(i-1,j,dp) + helper(i,j-1,dp)
		
		return dp[i][j]

	return helper(m-1,n-1,dp)

	# tabulation

	dp = [[0]*(n) for _ in range(m)] 

	for i in range(0,m):
		for j in range(0,n):
			# print(i,j)
			if i == 0 and j == 0:
				dp[i][j] = 1
			elif i == 0:
				dp[i][j] = dp[i][j-1]
			elif j == 0:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
	
	return dp[m-1][n-1]

	# space optimization

	prev = [0]*(n) 

	for i in range(0,m):
		curr = [0]*n
		for j in range(0,n):
			# print(i,j)
			if i == 0 and j == 0:
				curr[j] = 1
			elif i == 0:
				curr[j] = curr[j-1]
			elif j == 0:
				curr[j] = prev[j]
			else:
				curr[j] = prev[j] + curr[j-1]
		
		prev = curr
	
	return curr[n-1]

	
