def find_in_mountain_array(arr, target):
    N = len(arr)

    def binary_search(low, high, target, is_ascending):
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid
            
            if is_ascending:
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    left, right = 0, N - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1 
        else:
            right = mid 
    
    peak_index = left

    result_left = binary_search(0, peak_index, target, is_ascending=True)
    if result_left != -1:
        return result_left

    result_right = binary_search(peak_index + 1, N - 1, target, is_ascending=False)
    
    return result_right

