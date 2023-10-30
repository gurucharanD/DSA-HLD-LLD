# the combinations should be in the sorted order
# inorder to have the duplicates side by side
# we need to sort the input array at the begining
# hence sort the input array before you create the combinations
#  to avoid duplicates, you need to consider all the elements
#  to be the starting element in the subset array
# if two adjacent elements in the candidate array are equal
# include the first one and dont include the second one
# and keep iterating over the array from current index to last index
# and keep backtracking
    

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        subsets = []
        
        def helper(subset,index,count):
                        
            if count == 0:
                subsets.append(subset.copy())
                return

            if count < 0:
                return
                
            for i in range(index,len(candidates)):

                # irrespective of if the element at index is a duplicate or not 
                # we can pick the element at the index, after picking the first 
                # element you cannot pick the duplicate element

                # the duplicate elements lie to the right side of the current index
                # so if you should always include the current index, if you 
                # are picking the current index for the first time and then check 
                # if you are including any duplicates hence we add the condition
                #  i > index 

                if i > index and candidates[i] == candidates[i-1]:
                    continue
                    
                subset.append(candidates[i])
                helper(subset,i+1,count-candidates[i])
                subset.pop()
                
        helper([],0,target)
        return subsets
        
        

        
        
        