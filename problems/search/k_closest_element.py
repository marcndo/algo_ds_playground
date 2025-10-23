def find_k_closest(arr, k, x):
    N = len(arr)
    left, right = 0, N - k
    
    while left < right:
        mid = (left + right) // 2
        if abs(arr[mid] - x) > abs(arr[mid + k] - x):
            left = mid + 1
        else:
            right = mid
            
    return arr[left : left + k]

