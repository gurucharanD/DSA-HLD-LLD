"""
# Definition for Employee.

class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
        
"""
# 690. Employee Importance

# create a hashmap of all the employees indexed by their id
# start doing bfs on the sub-ordinates of the id that is passed 
# and keep adding up the importance of each node

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        map_emp = {}
        
        for e in employees:
            map_emp[e.id] = e
        
        importance = 0
        queue = [map_emp[id]]
        
        while len(queue) != 0:
            node = queue.pop(0)
            importance += node.importance
            subs = node.subordinates
            for sub in subs:
                queue.append(map_emp[sub])
                
        return importance
            
        
            
        
        