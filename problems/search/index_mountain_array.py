def find_pick_index(arr):
    peak_index = {}
    length = len(arr)
    for i in range(length):
        for j in range(i+1, length):
            if arr[i] > arr[j]:
                peak_index[arr[i]] = i 
                break
    
    return max(peak_index.items())[1]
         
array = [1, 2, 3, 4, 2, 1, 0]

def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid 
    return right




print(find_pick_index(array))
print(peakIndexInMountainArray(array))
