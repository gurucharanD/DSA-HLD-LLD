# 311. Sparse Matrix Multiplication

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        def compressMatrix(mat):
            r = len(mat)
            c = len(mat[0])
            
            compMat = [[] for _ in range(r)]
            
            for i in range(r):
                for j in range(c):
                    
                    if mat[i][j]:
                        compMat[i].append((mat[i][j],j))
            
            return compMat
        
        comp_mat1 = compressMatrix(mat1)
        comp_mat2 = compressMatrix(mat2)
        
        print(comp_mat1)
        print(comp_mat2)
        
        rows1 = len(mat1)
        cols1 = len(mat1[0])
        rows2 = len(mat2)
        cols2 = len(mat2[0])
        ans = [[0]*cols2 for _ in range(rows1)]
        
        for r in range(rows1):
            for ele1,mat1Col in comp_mat1[r]:
                for ele2,mat2Col in comp_mat2[mat1Col]:
                    ans[r][mat2Col] += ele1*ele2
            
        return ans
                    
            