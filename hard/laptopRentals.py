# bruteforce solution :
# sort the given time intervals with by their start time
# loop over the input array and find if there is an overlap with 
# the intervals before, if there is a overlap increase the laptop counter
# else do nothing 

# time = O(n^2) and O(1) space

def laptopRentals(times):

	if len(times) == 0:
		return 0
	
	laptopsCounter = 1
	startTime = 0
	endTime = 1
	# endedTasks = [None for _ in range(len(times))]
	times.sort(key = lambda x:x[0])
	print(times)
	for i in range(1,len(times)):
		currentSlot = times[i]
		overLap = False
		for j in range(i-laptopsCounter,i):
			previousSlot = times[j]
			if currentSlot[startTime] < previousSlot[endTime]:
				overLap = True
			else:
				overLap = False
				# del times[j]
				break
				
		if overLap:
			laptopsCounter+=1
		print(overLap,laptopsCounter,times)
    return laptopsCounter


# optimised solution:
# sort the time intervals by their start time
# build a minheap by their ending time

# insert the first element into the 
# compare the ending time of the interval on top 
# of the heap, to the starting time of the interval at i
# if the interval on top of the heap finsihes before the interval at i
# we can use the laptop and remove the interval from the heap and insert new interval on to the heap
# else we need to insert the new interval on
# to the tree
# at the end of the iteration, the minheap has the tasks
# that are running at the same time and the number of laptops needed
# is equal to the length of the heap
# the size of the minHeap shows the max overlap size

# heap gives us access to the interval that ends first 
# so we dont have to look at all the intervals before i 
# to check if there is a task that ends before it
# hence we can get rid of our n squared complexity

# space = O(N) as we are using a heap
# time = O(NlogN) as we are sorting and accessing the heap N times adds another NlogN time
# so, we get 2NlogN complexity

def laptopRentals(times):
    # Write your code here.
	if len(times) == 0:
		return 0
	
	laptops = 0
	startTimes = [x[0] for x in times]
	endTimes = [x[1] for x in times]
	
	startTimes.sort()
	endTimes.sort()
		
	pointer1 = 0
	pointer2 = 0
	
	while pointer1 < len(times):
		if startTimes[pointer1] >= endTimes[pointer2]:
			laptops-=1
			pointer2 += 1
		
		laptops += 1
		pointer1 += 1



    return laptops
