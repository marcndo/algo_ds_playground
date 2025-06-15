import random
"""
Question: https://leetcode.com/problems/sort-an-array/description/
Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
FUNCTION heap_sort(arr)
    n = len(arr)
    IF n <= 1
        RETURN arr
    END IF
    FOR i FROM n/2 - 1 to 0
        heapify(arr, size, i)
    END FOR
    FOR i FROM n-1 DOWNTO 0
        heapify(arr, size, 0)
        swap arr[i], arr[0]
    END FOR
    RETURN arr
END FUNCTION

FUNCTION heapify(arr, size, i)
    largest <-- i
    left <-- 2*i+1
    right <-- 2*i+2
    IF i < left AND arr[left] > arr[largest]
        largest <-- left
    END IF
    IF i < right AND arr[right] > arr[largest]
        largest <-- right
    END IF
    IF i != largest
        swap arr[i] with arr[largest]
        heapify(arr, size, largest)
"""


def sort_array(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        heapify(arr, n, 0)
        arr[i], arr[0] = arr[0], arr[i]
    return arr


def heapify(arr, size, i):
    largest = 0
    left = 2 * i + 1
    right = 2 * i + 2
    if i <= left and arr[i] > arr[largest]:
        largest = left
    if i <= right and arr[i] > arr[largest]:
        largest = right

    if i != largest:
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, size, 0)


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
    print(sort_array(case))
    print("\n")