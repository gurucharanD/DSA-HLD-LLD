# bruteforce, O(n) time and O(n) space
import math

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
		self.max = float("-inf")
		self.array = []

    def insert(self, number):
		
		if len(self.array) == 0:
			self.array.append(number)
			self.max = number
			self.calulateMedian()
			return
		
		if number >= self.max:
			self.array.append(number)
			self.max = number
		else:
			queue = []
			i = len(self.array) - 1
			
			while self.array[i] >= number and i>=0:
				queue.append(self.array.pop())
				i-=1
			
			self.array.append(number)
			
			j = len(queue)-1
			
			while j>=0:
				self.array.append(queue.pop())
				j-=1
			
		self.calulateMedian()
		return
		
    def getMedian(self):
		# print(self.array)
        return self.median
	
	def calulateMedian(self):
		length = len(self.array)
		low = 0
		high = length - 1
		index = (low+high)/2

		if length % 2 == 0:
			self.median = ( self.array[math.ceil(index)] + self.array[math.floor(index)] )/2
		else:
			self.median = self.array[(low+high)//2]
		
		return


# optimised way is to use, min and max heaps
# insertion in heap is O(logn) , it is O(n) in arrays

# in an array, median is the average of the middle two elements if the array is even length 
# else the first element in the second half of the array

# we can find these two elements by building a min and max heaps

# if we build a max heap of the lower half of elements, we will find the first element
# if we build a min heap of the second half of elements, we will find the second Element

# if the array is even length , we return averge of these two
# else we return top value of the min heap

# the first element can go into min or max heap randomly, the following elements
# go into either of them based on the value, if its greater than the element we already know,
# they go into max heap, else they go into min heap

# as you keep iterating over the array, calculate the median at each iteration

# at any point, if the difference between the no of nodes in both the heaps
# is greater than 1, we need to re-balance the trees, remove nodes form tree that has more nodes
# and add them to the tree with less number of nodes

# insert and remove and rebalance will only cost O(logN) in heaps
# time is O(logN) and space is O(N)

def MAX_HEAP_FUNC(a,b):
	return a>b

def MIN_HEAP_FUNC(a,b):
	return a<b

class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
		self.lowers = Heap(MAX_HEAP_FUNC,[])
		self.greaters = Heap(MIN_HEAP_FUNC,[])

    def insert(self, number):
		if not self.lowers.length or number < self.lowers.peek():
			self.lowers.insert(number)
		else:
			self.greaters.insert(number)
			
		self.rebalanceHeaps()
		self.updateMedian()
	
	def updateMedian(self):
		if self.lowers.length == self.greaters.length:
			self.median = (self.lowers.peek() + self.greaters.peek())/2
		elif self.lowers.length > self.greaters.length:
			self.median = self.lowers.peek()
		else:
			self.median = self.greaters.peek()
			
	def rebalanceHeaps(self):
		if self.lowers.length-self.greaters.length == 2:
			self.greaters.insert(self.lowers.remove())
		elif self.greaters.length-self.lowers.length == 2:
			self.lowers.insert(self.greaters.remove())

		
    def getMedian(self):
        return self.median

	

class Heap:
	
    def __init__(self,comparisonFunc, array):
		self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
		self.length = len(self.heap)

    def buildHeap(self, array):
		firstParentIndex = (len(array)-2)//2
		for currentIndex in reversed(range(firstParentIndex+1)):
			self.siftDown(currentIndex,len(array)-1,array)
		
		return array

    def siftDown(self,currentIndex,endIndex,heap):
		childOneIndex = 2*currentIndex + 1
		
		while childOneIndex <= endIndex :
			childTwoIndex = 2*currentIndex + 2 if 2*currentIndex + 2 <= endIndex else -1
            
			if childTwoIndex != -1:
				if self.comparisonFunc(heap[childTwoIndex], heap[childOneIndex]):
					indexToSwap = childTwoIndex
				else:
					indexToSwap = childOneIndex
			else:
				indexToSwap = childOneIndex

			if self.comparisonFunc(heap[indexToSwap], heap[currentIndex]):
				self.swap(currentIndex,indexToSwap,heap)
				currentIndex = indexToSwap
				childOneIndex = 2*currentIndex + 1
			else:
				return


    def siftUp(self,currentIndex,heap):
		parentIndex = (currentIndex - 1)//2
		while currentIndex > 0:
			if self.comparisonFunc(heap[currentIndex] , heap[parentIndex]):
				self.swap(currentIndex,parentIndex,heap)
				currentIndex = parentIndex
				parentIndex = (currentIndex-1)//2
			else:
				return
			
    def peek(self):
		return self.heap[0]

    def remove(self):
		self.swap(0,len(self.heap)-1,self.heap)
		elementToRemove = self.heap.pop()
		self.length-=1
		self.siftDown(0,len(self.heap)-1,self.heap)
		return elementToRemove
		

    def insert(self, value):
		self.heap.append(value)
		self.length+=1
		self.siftUp(len(self.heap)-1,self.heap)
		
	def swap (self,i,j,heap):
		heap[i],heap[j] = heap[j],heap[i]