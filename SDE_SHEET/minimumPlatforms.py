# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]


arr = [900, 1100, 1235]
dep = [1000, 1200, 1240]

arr.sort()
dep.sort()

i = 1
j = 0
ans = 1
count = 1

n = len(arr)

while i < n and j < n:
    # we have another train arriving at the platform
    # before the first train is leaving
    # hence we increment the count of platforms
    if arr[i] <= dep[j]:
        count+=1
        i+=1
    else:
        count -= 1
        j += 1
    
    ans = max(ans,count)

print(ans)