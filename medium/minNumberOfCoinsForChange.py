# dynamic programming

# similar approach as numberOfWaysToMakeChange,
# except initialise the array with infinity this time

# but the recurrence changes ,

# ways[i] = min(ways[amount],ways[amount-denom]+1)

# O(ND) time and O(N) space

def minNumberOfCoinsForChange(n, denoms):
	
	ways = [float("inf") for i in range(0,n+1)]
	ways[0] = 0
	
	for denom in denoms:
		for amount in range(len(ways)):
			if denom <= amount:
				ways[amount] = min( ways[amount], ways[amount-denom]+1 )
			
	if ways[n] != float("inf"):
		return ways[n]
	else:
		return -1





