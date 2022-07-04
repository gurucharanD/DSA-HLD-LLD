# 135. Candy
# brute force
# O(n^2)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1 for _ in range(len(ratings))]
        
        for i in range(1,len(ratings)):
            curr = ratings[i]
            prev = ratings[i-1]
            
            if curr < prev:
                index = i
                c = curr
                p = prev
                
                while c < p and index > 0:
             
                    if res[index-1] <= res[index]:
                        res[index-1]+=1
                        
                    index -= 1
                    c = ratings[index]
                    p = ratings[index-1]
                    
            elif curr > prev:
                res[i] = 1+res[i-1]
                
        return sum(res)


# two pass 
# O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1 for _ in range(len(ratings))]
        
        for i in range(0,len(ratings)-1):
            curr = ratings[i]
            nxt = ratings[i+1]
                        
            if nxt > curr:
                res[i+1] = 1+res[i]
        
        for i in range(len(ratings)-1,0,-1):
            curr = ratings[i]
            prev = ratings[i-1]
                        
            if prev > curr:
                res[i-1] = max(res[i-1], 1+res[i])
            
        return sum(res)
    
    
    
                
                
        
    
    
