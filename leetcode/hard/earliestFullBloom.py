# greedy algorithm
# since we need the shortest time , we need to start with the
# plant with max growth or plant time
# sort the plants by growth time desc and plant time desc
# check the solution for which one gives the min time

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        
        plant_grow = [(plantTime[i],growTime[i]) for i in range(len(plantTime))]
        plant_grow.sort(key = lambda x:-x[1])

        start_day = 0
        ans = 0
        
        for plant,grow in plant_grow:
            bloom_day = start_day + plant + grow 
            ans = max(ans,bloom_day)
            start_day += plant
        
        return ans