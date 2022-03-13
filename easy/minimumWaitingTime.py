def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	waitingTimeForEach = 0
	totalWaitingTime = 0
	
	print(queries)
	
	for i in range(len(queries)-1):
		waitingTimeForEach = waitingTimeForEach + queries[i]
		totalWaitingTime +=  waitingTimeForEach
		print(waitingTimeForEach)
		
    return totalWaitingTime



# sort the tasks in ascending order 

# the firsttask has a waitng Time of 0

# at ecach task find the waiting time for it 
# and add its waiting time to totalWaitingTime

# tasks = [1, 2, 2, 3, 6]
# wait  = [0, 1, 3, 5, 8]