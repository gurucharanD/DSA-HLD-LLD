# Find number of times a string occurs as a subsequence in given string
# answer = 7
# string1 = "subsequence"
# string2 = "sue"

# O(m*n) time and space

answer = 2
string1 = "subsequence"
string2 = "seq"

# answer = 4
# string1 = "GeeksforGeeks"
# string2 = "Gks"

matrix = [[0 for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]

for i in range(len(matrix)):
    matrix[i][0] = 1 
    
for i in range(1,len(string1)+1):
    for j in range(1,len(string2)+1):
        if string1[i-1] == string2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
        else:
            matrix[i][j] = matrix[i-1][j]


for i in matrix:
    print(i)
    

print(matrix[len(matrix)-1][len(matrix[0])-1])
