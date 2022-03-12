def nonConstructibleChange(coins):
    # Write your code here.
	coins.sort();
	currentChange = 0;
	for coin in coins:
		if coin > currentChange+1:
			return currentChange +1
		currentChange+=coin
	
    return currentChange+1


# comments
# for every coin that you add check if it is greater than 
# currentChange+1
# if it is greater then you cant construct currentChange+1
# else increment the currentChange by the current coin value

