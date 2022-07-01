subsets = []
def sumTok(subset,index,array,sum,count):
    
    if index == len(array):
        
        if count == sum:
            subsets.append(subset[:])
        
        return
    
    if count > sum:
        return
    
    sumTok(subset,index+1,array,sum,count)
    count+=array[index]
    subset.append(array[index])
    sumTok(subset,index+1,array,sum,count)
    count-=array[index]
    subset.pop()
    
    return
    

sumTok([],0,[1,2,3,4],2,0)
print(subsets)


# return only one subsequence
subsets = []
def sumTok(subset,index,array,sums,count):
    
    if index == len(array):
        
        if count == sums:
            return subset
        
        return None
    
    if count > sums:
        return
    
    if sumTok(subset,index+1,array,sums,count):
        return subset
        
    count+=array[index]
    subset.append(array[index])
        
    if sumTok(subset,index+1,array,sums,count):
        return subset
        
    count-=array[index]
    subset.pop()
    
    return None
    

print(sumTok([],0,[1,2,3,4],3,0))
# print(subsets)


            