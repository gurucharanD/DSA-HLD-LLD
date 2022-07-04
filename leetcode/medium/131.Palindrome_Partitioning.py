# 131. Palindrome Partitioning
# Place the partition at an index, breaking the string into two parts
# such that the left part of the string should be a palindrome
# once the left part is a palindrome, invoke the same function on the 
# remaining substring on the right
 


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        solution = []
        def helper(subsets,index,string):
        
            if index == len(string):
                solution.append(subsets[:])
                return
            
            for i in range(index,len(string)):
                curr = string[index:i+1]
                if curr == curr[::-1]:
                    subsets.append(curr)
                    helper(subsets,i+1,string)
                    subsets.pop()

        helper([],0,s)
        return solution
                
                            
            
            
        