def longestPalindromicSubsequence(string):
    matrix = [[0 for _ in range(len(string)+1)] for _ in range(0,len(string)+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j :
                matrix[i][j] = 1

    
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if string[i-1] == string[j-1] :
                matrix[i][j] = matrix[i+1][j-1]+2
            else:
                matrix[i][j] = max( matrix[i][j-1], matrix[i+1][j])

    
    print(matrix)

    return
