# 406. Queue Reconstruction by Height
# sort the arrays before you do anything 
# it gives some ideas

# sort the input array based on the second key
# identify the difference between the number of people required to satisfy the condition and the current count that satisfies the condition
# the difference gives the number of forward swaps ( i.e the number by the which the current postion is off by )
# O(n^2) time and O(1) space

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key=lambda k: (k[1]))
        
        for i in range(0,len(people)):
            currentPerson = people[i]
            count = 0
            noOfSwaps = 0
            for j in range(0,i):
                if people[j][0] >= currentPerson[0]:
                    count+=1
                
            noOfSwaps = abs(currentPerson[1]-count)
            
            currIndex = i
            while noOfSwaps!=0:
                prevIndex = currIndex-1
                people[currIndex],people[prevIndex] = people[prevIndex],people[currIndex]
                currIndex = prevIndex
                noOfSwaps -= 1
    
        return people
                
