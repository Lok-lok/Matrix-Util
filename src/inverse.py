import transpose
import determinant
import cofactor
import multiply

def inverse(matrix):
    """
        Cramer's rule
        
        The time complexity increases exponentially as the size of matrix increases
    """
    cofactor_matrix = cofactor.cofactor(matrix)
    transpose_matrix = transpose.transpose(cofactor_matrix)
    
    matrix_determinant = determinant.determinant(matrix, 0, list(range(len(matrix[0]))))
    for i in range(len(transpose_matrix)):
        for j in range(len(transpose_matrix[i])):
            transpose_matrix[i][j] /= matrix_determinant
    return transpose_matrix