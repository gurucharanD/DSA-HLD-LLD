# find the building less than the height of the current building to its left
# find the building less than the height of the current building to its right

# find the distance between these two buildings and multiply the height of the building
#  this gives the area of the rectangle formed
#  the rectangle with max area is the required rectangle


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0 for _ in heights]
        right = [0 for _ in heights]
        
        stack = []
        
        for i in range(0,len(heights)):
        
            while len(stack) and heights[stack[-1]] >=  heights[i]:
                stack.pop()
            
            if not stack:
                left[i] = 0
            else:
                left[i] = stack[-1]+1
                
            stack.append(i)
            
        
        stack = []

        for i in range(len(heights)-1,-1,-1):
        
            while len(stack) and heights[stack[-1]] >=  heights[i]:
                stack.pop()
            
            if not stack:
                right[i] = len(heights)-1
            else:
                right[i] = stack[-1]-1
                
            stack.append(i)
            
        print(left)
        print(right)
        
        ans = 0
        for i in range(0,len(heights)):
            ans = max(ans,heights[i]*(right[i]-left[i]+1))
        
        return ans
        

        

            
            
