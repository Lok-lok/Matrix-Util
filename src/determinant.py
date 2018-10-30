def determinant(matrix, row_index, available_column):
    """
        n x n matrix only
    """
    if len(matrix) != len(matrix[0]):
        return None
    
    if row_index == len(matrix) - 1:
        return matrix[row_index][available_column[0]]
        
    sum = 0
    next_row_index = row_index + 1
    sign = 1
    
    for k in available_column:
        next_available_column = available_column.copy()
        next_available_column.remove(k)
        sum += sign * matrix[row_index][k] * determinant(matrix, next_row_index, next_available_column)
        sign = 0 - sign
        
    return sum