def search_matrix(matrix, target):
    rows = len(matrix) 
    columns = len(matrix[0])
    if not matrix or not matrix[0]:
        return False
    elif matrix[rows - 1][columns - 1] < target:
        return False
    i = 0
    j = columns - 1
    while i < rows and j >= 0:
        current_val = matrix[i][j]
        if current_val == target:
            return True
        elif current_val < target:
            i += 1
        else:
            j -= 1
    return False
