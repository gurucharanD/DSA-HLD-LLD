def getLowestCommonManager(topManager, reportOne, reportTwo):

	pathToOne = findPath(topManager, reportOne)
	pathToTwo = findPath(topManager, reportTwo)   
	
	actualPathToOne = findActualPath(pathToOne,reportOne)
	actualPathToOne.append(reportOne)
	
	actualPathToTwo = findActualPath(pathToTwo,reportTwo)
	actualPathToTwo.append(reportTwo)
	
	if len(actualPathToOne) == 0:
		return actualPathToTwo[0]
	elif len(actualPathToTwo) == 0:
		return actualPathToOne[0]
	
	if len(actualPathToOne) == 1:
		return actualPathToOne[0]
	elif len(actualPathToTwo) == 1:
		return actualPathToTwo[0]
	
	pointer1 = 0
	pointer2 = 0
	while pointer1 < len(actualPathToOne) and pointer2 < len(actualPathToTwo):
		print(actualPathToOne[pointer1].name,actualPathToTwo[pointer2].name)
		if actualPathToOne[pointer1] != actualPathToTwo[pointer2]:
			return actualPathToOne[pointer1-1]
		
		pointer1+=1
		pointer2+=1
	
	return actualPathToOne[pointer1-1]

# This is an input class. Do not edit.


def findActualPath(path,target):
	actualPath = []
	while len(path) > 0:
		currentNode = path.pop()
		if target in currentNode.directReports:
			actualPath.append(currentNode)
			target = currentNode
	return list(reversed(actualPath))

def findPath(source,target):
	queue = [source]
	path = []
	while len(queue)!=0:
		currentNode = queue.pop(0)
		if currentNode.name == target.name:
			break
		else:
			path.append(currentNode)
		for report in currentNode.directReports:
			queue.append(report)
	
	return path
	
	
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
