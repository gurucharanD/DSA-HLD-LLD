def longCommonSubString(string1,string2):

    matrix = [[0 for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):

            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]+1
          
    for k in matrix:
        print(k)

longCommonSubString('GeeksforGeeks','GeeksQuiz')
