import random
"""
[38, 27, 43, 3, 9, 82, 10]
FUNCTION quick_sort(arr)
    array_length <-- array length
    IF array_length <= 1
        RETURN arr
    pivot <-- last element of array
    less_than_pivot <-- empty list
    greater_than_pivot <-- empty list
    FOR each element x in array excluding last element
        IF x <= pivot
            add x in less_than_pivot
        ELSE
            add x to greater_than_pivot
        END IF
    END FOR
    RETURN quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
"""


def quick_sort(arr):
    array_length = len(arr)
    if array_length <= 1:
        return arr
    pivot = arr[-1]
    less_than_pivot = []
    greater_than_pivot = []
    for i in range(array_length-1):
        if arr[i] <= pivot:
            less_than_pivot.append(arr[i])
        else:
            greater_than_pivot.append(arr[i])
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


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
    print(quick_sort(case))
    print("\n")