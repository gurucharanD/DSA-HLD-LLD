def threeNumberSum(array, targetSum):
	triplets = [];
	array.sort();
	
	for i in range(len(array)):
		left = i+1;
		right = len(array)-1;
		while( left<right ):
			cuurSum = array[i]+array[left]+array[right]
			if( cuurSum == targetSum ):
				triplets.append([array[i], array[left], array[right]]);
				left+=1
				right-=1
			elif( cuurSum<targetSum ):
				left+=1
			elif( cuurSum > targetSum):
				right-=1
			
				
	
	
	return triplets
		
		

# sort the array in the begining as the outpuut is expected to be sorted.

# start looping over the array and for each element find 

# if there exists 2 elements from index + 1 of that element to length of array -1 

# since the array is sorted, the chances of an element falling to the left of the current index is zero

# because we might have already checked such scenario in the iteration from first index

# since the array is sorted, use two pointer technique to loop over the array to find the remanining two elements

# that can contribute to the sum
    
