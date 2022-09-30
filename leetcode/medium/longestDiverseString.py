class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        # push all elements on to maxheap
        # pick the largest element from heap and place it in array      
        # until the element cannot be placed in the array anymore
        # push the element back onto the heap with reduced count   
        # when the element cannot be placed in the array anymore
        # go for the next greater character 
        
        maxHeap = []
        heapify(maxHeap)
        
        if a!=0:
            heappush(maxHeap,(-1*a,'a'))
        if b!=0:
            heappush(maxHeap,(-1*b,'b'))
        if c!=0:
            heappush(maxHeap,(-1*c,'c'))
            
        arr = []
        while maxHeap:
            
            count,char= heappop(maxHeap)
            
            if len(arr) > 1 and arr[-1] == char and arr[-2] == char:
                
                    if not maxHeap:
                        return "".join(arr)
                    
                    secondCount,secondChar = heappop(maxHeap)
                    arr.append(secondChar)
                    secondCount+=1
                    if secondCount:
                        heappush(maxHeap,(secondCount,secondChar))
                    # we push the current character and count at the end
                    # because we dont want the same character to come up again
                    # if it still has the max count, we basically want the character
                    # with max count after the current element                       
                    if count:
                        heappush(maxHeap,(count,char))
            else:
                
                    arr.append(char)
                    count+=1
                    if count:
                        heappush(maxHeap,(count,char))
                        
        return "".join(arr)
            


        
        