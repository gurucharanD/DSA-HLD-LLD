
subsets = []

def powerset(subset,index,array):
    
    if index >= len(array):
        print(subset)
        return
    
    powerset(subset,index+1,array)
    subset.append(array[index])
    powerset(subset,index+1,array)
    subset.pop()
    return
    

powerset([],0,[1,2,3])

        
    