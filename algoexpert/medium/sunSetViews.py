# bruteforce approach is to
# compare each building to all
# the other buildings this ends up giving a complexity of O(n^2)

#______

# the other solution in O(n) is to 

# start iterating the buildings in the oppiste direction

# i.e if the buildings are facing in the EAST (right) direction
# iterate from right to left (WEST)

# if the buildings are facing in the WEST (left) direction
# iterate from left to right(EAST)


# and at every point keep track of the maximum height which is 0 intially and
# check if the height of the building is greater than the current maximum height

# if yes, then the building can see the sunlight add the building to the solution
#  and update the maximum height

def sunsetViews(buildings, direction):
	# solution 1 using running maximum height
	# we start from east and go to west if direction is east
	# we start from west and go to east if direction is west
	
	# if len(buildings) == 1 or len(buildings) == 0:
	# 	return buildings
	
	currentMaxHeight  = 0;
	startIndex = 0;
	step = 1;
	solution = []
	
	if direction == "EAST":
		startIndex = len(buildings)-1;
		step = -1;
		
	while startIndex >= 0 and startIndex < len(buildings):
		if(buildings[startIndex]>currentMaxHeight):
			solution.append(startIndex);
			currentMaxHeight = buildings[startIndex]
		
		startIndex+=step
	
	if direction == "EAST":
		solution.reverse()
	
	return solution

# ______

# the other solution is to use a stack to keep track of 
# all the buildings that can see the sunset, looping in the direction 
# that the buildings are facing, a building can see the sunset only
# if the buildings that are next to it are smaller than the current building

# so, if the height od current building is greater than the building that is currently
# located on top of the stack, we remove the element from the stack and push the current
# building onto the stack

# O(n) time and space for stack

# the push and pop opeartions onto stack may take
# extra time but in the entire traversal we may push atmost n elements
# on the stack -> so we may end up with O(2n)
#  ignoring the constants we get O(n)
# ______


def sunsetViews(buildings, direction):
	
	stack = [];
	startIndex  = 0 if direction == "EAST" else len(buildings)-1;
	step = 1 if direction == "EAST" else -1;
		
	while startIndex >=0 and startIndex < len(buildings) :
		
		buildingHeight = buildings[startIndex]
		
		while len(stack)>0 and buildingHeight >= buildings[stack[-1]]:
			stack.pop()
		
		stack.append(startIndex);
		startIndex+=step
	
    
	if direction == "WEST":
		stack.reverse()
	
	return stack;



