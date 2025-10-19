def peak_index(arr):
    if len(arr) < 3:
        return -1
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i+1]:
            return i
    return len(arr) - 1


def peakIndex(arr):
    if len(arr) < 3:
        return - 1
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid 
    return left
