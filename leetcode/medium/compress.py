# 443. String Compression
# use two pointers
# where left always points to the index
# where you want to insert the next element
# either its a number or a character

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left = 0
        right = 1
        currentChar = chars[0]
        count = 1
        
        for index in range(1,len(chars)):
            
            if chars[index] == currentChar:
                count+=1
            else:
                chars[left] = currentChar
                left += 1
                if count > 1:
                    for c in list(str(count)):
                        chars[left] = c
                        left+=1
                        
                currentChar = chars[index]
                count = 1
            
        chars[left] = currentChar
        left += 1
        if count > 1:
            for c in list(str(count)):
                chars[left] = c
                left+=1
        
        return left