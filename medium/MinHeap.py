# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
		firstParentIndex = (len(array)-1)//2
		for currentIndex in reversed(range(firstParentIndex)):
			self.siftDown(currentIndex,len(array)-1,array)
		
		return array

    # def siftDown(self,currentIndex,endIndex,heap):
	# 	childOneIndex = 2*currentIndex + 1
	# 	childTwoIndex = 2*currentIndex + 2
		
	# 	while currentIndex <= endIndex and childOneIndex <= endIndex and childTwoIndex <= endIndex:

	# 		smallestChildIndex = childOneIndex if heap[childOneIndex] <= heap[childTwoIndex] else childTwoIndex
			
	# 		if heap[smallestChildIndex] < heap[currentIndex]:
	# 			self.swap(smallestChildIndex,currentIndex,heap)
	# 			currentIndex = smallestChildIndex
	# 			childOneIndex = 2*currentIndex + 1
	# 			childTwoIndex = 2*currentIndex + 2
	# 		else:
	# 			break

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