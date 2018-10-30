def multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
        
    result = [[0 for j in matrix2[0]] for i in matrix1]
    for i in range(len(result)):
        for j in range(len(result[i])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    return result