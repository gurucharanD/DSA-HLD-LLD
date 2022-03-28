from signal import pthread_kill
from pandas import array


def longestPeak(array):
    # Write your code here.
	peaks = []
	
	for i in range(1,len(array)-1):
		if(array[i]>array[i-1] and array[i]>array[i+1]):
			peaks.append(i);
		
	# print(peaks)
	
	maxPeak = 0;
	
	for i in range(len(peaks)):
		currentPeak = peaks[i];
		left = currentPeak-1
		right = currentPeak+1
		
		while(left > 0 and array[left-1]<array[left]):
			left-=1
			
		while(right < len(array)-1 and array[right+1]<array[right]):
			right+=1
			
		peakLength = (right-left)+1
		
		if(peakLength>maxPeak):
			maxPeak = peakLength
		
		
		
		
    return maxPeak




# an element is said to be peak, if it is greater than the element 
# to the left of it and to the element to the right of iter

# using this identify all the peaks in the given array

# after finding the peaks, find the length of each peak,
# the element next to the left and to the right of the peak should be decreasing 
# keep moving to left and right until this condition is not satisifed.

# after stopping find the diferrence between left and right that gives the length of pthread_kill
# using this identify the length of all the peaks and find the max peak among all the peaks