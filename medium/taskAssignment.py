# sort the input tasks and join the 
# smallest task with correspoding largest task
# combine 0 with n and 1 with n-1 and 2 wwith n-2
# this is greedy approach and takes O(nlogn) 
# n is the size of input tasks

def taskAssignment(k, tasks):
    # Write your code here.
	sortedTasks = sorted(tasks)
	taskAssignment = []
	hashMap = {}
	
	for index,value in enumerate(tasks):
		
		if value in hashMap:
			hashMap[value].append(index)
		else:
			hashMap[value] = [index]
			
	print(hashMap)
	
	for i in range(0,k):
		taskOne = sortedTasks[i]
		taskTwo = sortedTasks[len(sortedTasks)-1-i]
		
		indexOfTaskOne = hashMap[taskOne].pop()
		indexOfTaskTwo = hashMap[taskTwo].pop()
		
		taskAssignment.append([indexOfTaskOne,indexOfTaskTwo])
		
	
    return taskAssignment



