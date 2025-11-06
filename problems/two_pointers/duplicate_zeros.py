def duplicate_zeros_brute_force(arr):
    result = []
    for num in arr:
        if num != 0:
            result.append(num)
        else:
            j = 0
            while j < 2:
                result.append(num)
                j += 1
    return result

def duplicate_zero_optimal(arr):
    n = len(arr)
    zeros = arr.count(0)
    i = n - 1
    j = n + zeros - 1
    while i >= 0:
        if j < n:
            arr[j] = arr[i]
        if arr[i] == 0:
            j -= 1
            if j < n:
                arr[j] = 0
        i -= 1
        j -= 1
    return arr





arr = [1,0,2,3,0,4,5,0]
print(duplicate_zeros_brute_force(arr))
print(duplicate_zero_optimal(arr))