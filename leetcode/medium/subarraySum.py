class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = defaultdict(int)
        
        sum = 0
        count = 0
        
        for num in nums:
            
            sum += num
            if sum == k:
                count+=1
            
            # no of times the prefix sum: 
            # sum - k ocuured 
            count += prefixSum[sum-k]
            prefixSum[sum]+=1
            
        return count

# nums = [1,2,3], k = 3

# intial hashMap will be empty  
# sum = 0 and count = 0
# index = 0
# sum = 1
# sum != 3

# sum-k = 1-3 = -2 doesnt exist as a prefix sum 
# hence count will be incremented by 0

# save the new sum which is a prefix sum and its count
# {1:1}

# index = 1
# sum = 3
# sum == k:
# count = 1
# sum - k = 0 doesnt exist in the prefixsum
# count will be incremented by 0
# {1:1,3:1}

# index = 2
# sum = 6
# sum != 3
# sum - k = 3 exists a prefix sum
# count will be incremented by 1
# save the new prefix sum to the hashmap
# {1:1,3:1,6:1}



            