# identify the character with most occurences 
# and place it in alternate positions in the input array
# i.e at 0 2 4 6 ..

# after placing the max character continue
# placing the next charaacter at alternate positions
# we place characters in alternate positions beacause we 
# may characters with more than count 1 and we should not
# place them together, hence we continue placing them in the 
# alternate positons

# if during this process if the index goes greater than len(s)
# which only happens once, move the index to 1
# and continue placing the characters

class Solution:

    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)
        maxChar = None
        maxCount = 0
        
        for key in counter:
            if counter[key] > maxCount:
                maxChar = key
                maxCount = counter[key]
            
            
        if maxCount > (len(s)+1)//2:
            return ""
    
        output = ['']*len(s)
        
        i = 0
        for _ in range(maxCount):
            output[i] = maxChar
            i+=2
        counter[maxChar] = 0
        
        for key in counter:
            if counter[key] > 0:
                
                for _ in range(counter[key]):
                    if i >= len(s):
                        i = 1
                    
                    output[i] = key
                    i+=2
        
        return "".join(output)
        
        
        