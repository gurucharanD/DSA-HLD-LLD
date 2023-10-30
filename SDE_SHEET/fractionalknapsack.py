class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        # we need to pick the items that have greater
        # value to weight ratio because we have limited weight
        # and we have to maximise the value
        
        arr.sort(key= lambda x:x.value/x.weight, reverse = True)
        
        occupiedValue = 0
        occupiedWeight = 0
        
        for item in arr:
            if occupiedWeight+item.weight<=w:
                occupiedValue+=item.value
                occupiedWeight+=item.weight
            else:
                remain = w-occupiedWeight
                occupiedValue+=(item.value)*(remain/item.weight)
                break
            
        return occupiedValue