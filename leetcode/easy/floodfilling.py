# 733. Flood Fill
# start dfs at the given source row and column
# and invoke dfs on the neighbours if the color of neighbours is equal to 
# the original color
# if the color of source row and col is already new color
# return the image

# here, we dont need to maintain visited array bcz
# if the child is already visited the color will be already changed from
# original color to new color

# we dont have to color a cell that doesnt have the original color
#  we only have to fill the cells that are connected to the given sr and sc
# in all four directions and having color as the image[sr][sc]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(i,j,originalColor,newColor,image):
            
            if i < 0 or j < 0: return
            if i >= len(image) or j >= len(image[0]): return
            if image[i][j] != originalColor : return

            image[i][j] = newColor
            dfs(i+1,j,originalColor,newColor,image)
            dfs(i,j+1,originalColor,newColor,image)
            dfs(i,j-1,originalColor,newColor,image)
            dfs(i-1,j,originalColor,newColor,image)
            
        if image[sr][sc] != newColor:
            dfs(sr,sc,image[sr][sc],newColor,image)
        return image

        