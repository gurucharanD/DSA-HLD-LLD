# # Dynamic Programming

# generate the possibilities of building the change from 0 to N ,
# where N is the change that is required to be build with the given denoms
# the array will be initialised to 0 first

# the reason for doing this => when we are buidling a change sometimes
# we will not have the exact denom and we end up having a remainder 
# to find the number of ways to build this remainder, this array will help us

# example: we are given N = 12 and denoms = 2,10

# no of ways = 1*12, 1*10+1*2

# when building the change with 10, the number of ways = 1 (since, 10 is less than 12 ) + no of ways to build 2

# therefore, the recurrence = 

# if amount <= denom:
#     ways[amount] = ways[amount] + ways[amount-denom]

# let amount = 12 and coin = 10

# ways[12] = ways[12] + ways[12-10] => ways[12] + ways[2]

# the element at the index of N is the number of ways we can build the change

# O(N.D) time, as we are iterating over the denoms array and ways array which has length N
#  and O(N) space


def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	ways = [ 0 for i in range(n+1)]
	ways[0] = 1
	
	for denom in denoms:
		for amount in range(1,len(ways)):
			
			if denom <= amount:
				ways[amount] += ways[amount-denom]

    return ways[n]


