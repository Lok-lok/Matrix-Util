import determinant

def cofactor(matrix):
    cofactor_matrix = [[0 for j in i] for i in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sub_matrix = []
            for row in matrix:
                sub_matrix.append(row.copy())
            sub_matrix.pop(i)
            for row in sub_matrix:
                row.pop(j)
            cofactor_matrix[i][j] = determinant.determinant(sub_matrix, 0, list(range(len(sub_matrix[0])))) * ((-1) ** (i + j))
    
    return cofactor_matrix