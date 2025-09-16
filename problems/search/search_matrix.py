def search_matrix(matrix, target):
    left, right = 0, len(matrix) * len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        num_col = len(matrix[0])
        row = mid // num_col
        col = mid % num_col
        current_val  = matrix[row][col]
        if current_val == target:
            return True
        elif current_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
