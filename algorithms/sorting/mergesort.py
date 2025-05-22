import random
"""
 [38, 27, 43, 3, 9, 82, 10]
 FUNCTION mergeSort(arr)
     array_length <-- len(arr)
     if array_length <= 1
         return arr
     mid <-- array_length // 2
     left <-- merge_sort(arr[:mid])
     right <-- merge_sort(arr[:right])
     RETURN merge(left, right)
END FUNCTION

FUNCTION merge(left, right)
    i <-- 0
    j <-- 0
    result <-- []
    WHILE i < len(left) AND j < len(right)
        IF left[i] < right[j]
            append left[i] to result
            i += 1
        ELSE
            append right[j] to result
            j += 1
        END IF
    END WHILE
    WHILE i < len(left)
        append left[i] to result
        i += 1
    END WHILE

    WHILE j < len(right)
        append right[j] to result
        j += 1
    END WHILE
    RETURN result
END FUNCTION
"""


def merge_sort(arr):
    array_length = len(arr)
    if array_length <= 1:
        return arr
    mid = array_length // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    i = j = 0
    result = []
    left_array_length = len(left)
    right_array_length = len(right)
    while i < left_array_length and j < right_array_length:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result




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
    print(merge_sort(case))
    print("\n")





