# since we want to delete the min num of elements
# sort the counts in desc order and start choosing the 
# largest elements in the sorted array, greedily

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        counts = {}
        for num in arr:
            if num in counts:
                counts[num]+=1
            else:
                counts[num] = 1
                
        counts = list(counts.values())
        counts.sort(reverse = True)
        
        deletedNumsSum = 0
        deletedNums = 0
        sumToDelete = sum(counts)//2
        i = 0
        
        while deletedNumsSum < sumToDelete:
            deletedNumsSum += counts[i]
            deletedNums+=1
            i+=1
        
        return deletedNums        
        
        