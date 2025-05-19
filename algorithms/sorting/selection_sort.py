import random
"""input:[5, 1, 4, 8, 2]
output: [1, 2, 4, 5, 8]
input: [9, 7, 3, 1]
output: [1, 3, 7, 9]
input: [1, 5, 6, 9]
output: [1, 5, 6, 9]
input: [1]
output: arr
input: []
output: arr
======================
input:[5, 1, 4, 8, 2] 1->[1, 5, 4, 8, 2] 2->[1, 2, 4, 8, 5]
min_val_index = 4
i = 3
j = 4
n = 5
========================
func selectionSort(arr)
    n = len(arr)
    for i in range(n)
    min_val_index = i
        for j in range(i+1, n)
            if arr[j] < arr[min_val_index]
                min_val_index = j
        if min_val_index != i
            arr[i], arr[min_val_index] = arr[min_val_index], arr[i]
        else:
        continue
"""


def selection_sort(arr):
    array_length = len(arr)
    if array_length == 0 or array_length == 1:
        return arr
    for i in range(array_length):
        min_val_index = i
        for j in range(i+1, array_length):
            if arr[j] < arr[min_val_index]:
                min_val_index = j
        if min_val_index != i:
            arr[i], arr[min_val_index] = arr[min_val_index], arr[i]
        else:
            continue
    return arr
                

array = random.sample(range(10), 10)
arr = [2, 8, 1, 3, 9]
arr1 = [1, 5, 6, 9]
arr2 = [1]
arr3 = []
test_cases = [arr, arr1, arr2, arr3]

for case in test_cases:
    print("Before sorting")
    print("==================")
    print(case)
    print("After sorting")
    print(selection_sort(case))
    print("\n")