# bruteforce: build a minHeap with all the elements in the array and 
# start removing the elements from the minHeap one by one and place them 
# in a array and return the array O(nlogn) time and O(n) space
# as we are iterating over the input array which is O(n) and insert into heap is O(logn) operation 
# we next iterate over the array again and reomove the elements from the heap, which is another O(nlogn) operation
# total time = O(2nlogn) => O(nlogn)
# doesnt depend on the value of K
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
		firstParentIndex = (len(array)-2)//2
		for currentIndex in reversed(range(firstParentIndex+1)):
			print(currentIndex)
			self.siftDown(currentIndex,len(array)-1,array)
		
		return array

    def siftDown(self,currentIndex,endIndex,heap):
		childOneIndex = 2*currentIndex + 1
		
		while childOneIndex <= endIndex :
			childTwoIndex = 2*currentIndex + 2 if 2*currentIndex + 2 <= endIndex else -1
            
			if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
				indexToSwap = childTwoIndex
			else:
				indexToSwap = childOneIndex
				
			if heap[indexToSwap] < heap[currentIndex]:
				self.swap(currentIndex,indexToSwap,heap)
				currentIndex = indexToSwap
				childOneIndex = 2*currentIndex + 1
			else:
				return


    def siftUp(self,currentIndex,heap):
		parentIndex = (currentIndex - 1)//2
		while currentIndex > 0 and heap[currentIndex] < heap[parentIndex]:
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
		return len(self.heap) == 0
		
def sortKSortedArray(array, k):
    # Write your code here.
	minHeap = MinHeap(array)
	print(minHeap.heap)
	output = []
	for i in range(0,len(array)):
		output.append(minHeap.remove())
	print(output)
    return output


# making use of K, we can identify that, the first element in the sorted array 
# lies between 0 to K, so we create a minHeap of elements from 0 to k, now the smallest 
# element in the array is in the heap
# and as we keep iterating from k+1 to end
# we keep removing the smallest element from the heap and push them into 
# output array,keep inserting new element into the heap
# once you have finished traversing k+1 to end
# remove remaining elements on heap and push them into output array

# the time reduces to O(nlogk) as we are iterating over the input array
# and we are adding and removing the elements into the heap, which will have only 
# K elements at any time
# we are using a heap of size K  so space is O(k)


def sortKSortedArray(array, k):
	# outPut = []
	minOfKandLen = min(k+1,len(array))
	minHeap = MinHeap(array[:minOfKandLen])
	index = 0
	for i in range(k+1,len(array)):
		array[index] = minHeap.remove()
		minHeap.insert(array[i])
		index+=1
		
	while not minHeap.isEmpty():
		array[index] = minHeap.remove()
		index+=1
		
	
	
	print(array)
	print(minHeap.heap)
	return array