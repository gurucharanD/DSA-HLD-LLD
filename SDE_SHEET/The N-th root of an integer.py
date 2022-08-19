N=5
M=32

low = 0
high = M

while low <= high:
    
    mid = (low + high) // 2
    
    ans = 1
    for i in range(N):
        ans *= mid
    
    if ans == M:
        print(mid)
        break
    
    if ans < M:
        low = mid
    else:
        high = mid
        
print(mid)
    