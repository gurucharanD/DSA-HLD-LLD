# when ever you are trying to find min no of something
# that is required based on time slots, use the 2 pointer approach
# since you already have time slost so you need atleast one thing
# so set your answer to 1 at the begining.
# sort the incoming times and outgoing times
# if there is another timeslot that is requiring the item before the 
# first item is returned then increase the items count

# sort the arrival time and departure times in ascending order
# since the time starts at the begining.
# if there is a train that is entering the station before the
# earliest train that is departing then we need an extra platfrom
# if there is no overlap we decrement the platform counter
# as we can reuse a platform at that point of time
# each iteration tells us how many platforms are needed at
# that point of time
 
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
    	platforms = 0
    	ans = 0
    	
    	startTimes = arr
    	endTimes = dep
    	
    	arr.sort()
    	dep.sort()
   
    	pointer1 = 0
    	pointer2 = 0
    	
    	while pointer1 < len(arr) and pointer2 < len(dep):
    		if arr[pointer1] <= dep[pointer2]:
    			platforms+=1
    			pointer1+=1
    		else:
        		platforms-=1
        		pointer2+=1
            
            ans = max(ans,platforms)
        
        return ans