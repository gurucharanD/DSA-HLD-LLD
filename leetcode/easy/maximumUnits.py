# 1710. Maximum Units on a Truck
# to maximise the no of units in truck, sort the input array by the number of units desc
# keep adding the units until the truck is full
# O(nlogn) time and O(1) space

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda k: (k[1]),reverse=True)
        maxResult = 0
        
        for i in range(0,len(boxTypes)):
            
            if truckSize <= 0:
                break            
                
            currBoxes,currUnits = boxTypes[i]
            
            if currBoxes >= truckSize:
                maxResult += (truckSize*currUnits)
            else:
                maxResult += currBoxes*currUnits
                
            truckSize-=currBoxes
            
        return maxResult