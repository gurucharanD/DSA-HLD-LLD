def findThreeLargestNumbers(array):
    # Write your code here.
	first = None;
	second = None;
	third = None;
	
	for number in array:
		if first is None or number > first :
			third = second
			second = first
			first = number
		elif second is None or number > second:
			third = second
			second = number
		elif third is None or number > third:
			third = number
			
	return [third,second,first];
