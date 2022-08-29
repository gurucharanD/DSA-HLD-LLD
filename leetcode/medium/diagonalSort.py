# traverse through first row and first column 
# sort the diagonal and save it to a hashmap
# traverse through the saved diagonals and rebuild the matrix

# number of digonals M = ( rows + cols - 1 )
# size of largest digonal = N = (no of rows)

# time = O(M*NlogN)
# space = O(M*N)



class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
                
        diagonals = {}
        
        def saveDiagonal(i,j) -> List[int]:
            diagonal = []
            while i < rows and j < cols:
                diagonal.append(mat[i][j])
                i+=1
                j+=1
            
            diagonal.sort()
            return diagonal
        
        def buildDiagonal(i,j,diagonal):
            while i < rows and j < cols:
                mat[i][j] = diagonal.pop(0)
                i+=1
                j+=1
            
        for j in range(cols):
            i = 0
            key = "{}-{}".format(i,j)
            diagonals[key] = saveDiagonal(i,j)
        
        for i in range(1,rows):
            j = 0
            key = "{}-{}".format(i,j)
            diagonals[key] = saveDiagonal(i,j)
                    
        for diag in diagonals:
            i,j = diag.split("-")
            i = int(i)
            j = int(j)
            buildDiagonal(i,j,diagonals[diag])

        return mat