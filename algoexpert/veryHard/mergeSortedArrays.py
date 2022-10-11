# Bruteforce: place pointers at the begining of each array 
# for k sorted arrays we would need k pointers
# find the smallest element of all the elements that the pointers are pointing to
# and place the smallest element of the k elements in the input array
# and increment the pointer that has given the smallest element

# this approach takes O(NK) n is the total number of elements 
# and K is the number of arrays. 
# for N elements we are making K comparisons to find the smallest element of the K 

# improved approach is to use a heap to find the minimum element among the K 
# we build the minHeap of the elements at index 0 of K arrays and 
# until the heap is empty we keep removing the smallest element from the heap
# we insert the element next to the smallest element in the array that the 
# current smallest number came from

# buidling the heap for K elements takes O(K) time
# finding the smallest element in the heap takes O(logk) for a heap of size K
# we do this for N elements, so the complexity becomes O(NlogK + K) 
# which is approx O(NlogK) and the space is O(K) for heap of size K






class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
		firstParentIndex = (len(array)-2)//2
		for currentIndex in reversed(range(firstParentIndex+1)):
			self.siftDown(currentIndex,len(array)-1,array)
		
		return array

    def siftDown(self,currentIndex,endIndex,heap):
		childOneIndex = 2*currentIndex + 1
		
		while childOneIndex <= endIndex :
			childTwoIndex = 2*currentIndex + 2 if 2*currentIndex + 2 <= endIndex else -1
            
			if childTwoIndex != -1 and heap[childTwoIndex]["num"] < heap[childOneIndex]["num"]:
				indexToSwap = childTwoIndex
			else:
				indexToSwap = childOneIndex
				
			if heap[indexToSwap]["num"] < heap[currentIndex]["num"]:
				self.swap(currentIndex,indexToSwap,heap)
				currentIndex = indexToSwap
				childOneIndex = 2*currentIndex + 1
			else:
				return

    def siftUp(self,currentIndex,heap):
		parentIndex = (currentIndex - 1)//2
		while currentIndex > 0 and heap[currentIndex]["num"] < heap[parentIndex]["num"]:
			self.swap(currentIndex,parentIndex,self.heap)
			currentIndex = parentIndex
			parentIndex = (currentIndex-1)//2
			
    def peek(self):
		return self.heap[0]

    def remove(self):
		self.swap(0,len(self.heap)-1,self.heap)
		elementToRemove = self.heap.pop()
		self.siftDown(0,len(self.heap)-1,self.heap)
		return elementToRemove
		
    def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap)-1,self.heap)
		
	def swap (self,i,j,heap):
		heap[i],heap[j] = heap[j],heap[i]
		
	def isEmpty(self):
		return len(self.heap)==0

def mergeSortedArrays(arrays):
	
	sortedList = []
	smallestItems = []
	for arrayIdx in range(len(arrays)):
		smallestItems.append(
			{
				"arrayIdx":arrayIdx,
				"elementIdx":0,
				"num":arrays[arrayIdx][0]
			}
		)
	
	minHeap = MinHeap(smallestItems)
	
	while not minHeap.isEmpty():
		smallestItem = minHeap.remove()
		arrayIdx,elementIdx,num = smallestItem["arrayIdx"],smallestItem["elementIdx"],smallestItem["num"]
		sortedList.append(num)
		
		if elementIdx == len(arrays[arrayIdx])-1:
			continue
		
		minHeap.insert({
			"arrayIdx":arrayIdx,
			"elementIdx":elementIdx + 1,
			"num":arrays[arrayIdx][elementIdx + 1]
		})
		
	return sortedList
	
