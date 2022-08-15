# Largest subarray with 0 sum

arr = [6, -2, 2, -8, 1, 7, 4, -10]
pfSum = 0
hashMap = {}
ans = 0

for i in range(0,len(arr)):
    pfSum+=arr[i]
    if pfSum == 0:
            # if prefix sum is 0 this means we have a subarray with 
            # sum 0, the length of the sub array will be current index + 1
            ans = i + 1; 
    else:
        if pfSum in hashMap:
            ans = max(ans,i-hashMap[pfSum])
        else:
            hashMap[pfSum] = i
        
print(ans)
print(hashMap)
        
