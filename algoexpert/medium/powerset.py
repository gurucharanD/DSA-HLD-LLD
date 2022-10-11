# keep adding elements to the 
# exisiting subsets that we created

def powerset(array):
    # Write your code here.
	subsets = [[]]
	for ele in array:
		for i in range(len(subsets)):
			print(subsets)

			currrentSubset = subsets[i]
			subsets.append(currrentSubset + [ele])

    return subsets
