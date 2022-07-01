# at every index you either pick the element or not pick the element
# if you pick the element, you again try to pick it
# if you dont pick the element, you go onto the next index

# O(2^t * k) time

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        solution = []
        def helper(subset,index,total,target,array,solution):
            
            if index >= len(array):
                if total == target:
                    solution.append(subset[:])
                    return
                
                return
                    
            if total > target:
                return
            
            #move to next element
            helper(subset,index+1,total,target,array,solution)
            
            total += array[index]
            subset.append(array[index])
            
            #pick the element again
            helper(subset,index,total,target,array,solution)
            
            total -= array[index]
            subset.pop()
            
              
            return 
        

        helper([],0,0,target,candidates,solution)
        return solution
