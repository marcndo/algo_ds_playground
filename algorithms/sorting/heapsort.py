import random
"""
Steps
=====================================================================================
Build a max heap(a binary tree whereby each parent node is greater than child node)
Swap the root(max) node with the last element in the heap
Reduce the heap size by one
Heapify to get a max heap
Repeat 2 to 4 until the heap size is 1
======================================================================================
FUNCTION heap_sort(arr)
    array_length = len(arr)
    IF array_length <= 1
        RETURN arr
    END IF
    FOR i FROM array_length/2 - 1 to 0
        heapify(arr, array_length, i)
    END FOR
    FOR i FROM n-1 to DOWNTO 1
      swap arr[0] with arr[i]
      heapify(arr,i,0)
    END FOR
    return arr
END FUNCTION

FUNCTION heapify(arr, size, i)
    largest ← i
    left ← 2 * i + 1
    right ← 2 * i + 2

    IF left < size AND arr[left] > arr[largest]
        largest ← left
    END IF

    IF right < size AND arr[right] > arr[largest]
        largest ← right
    END IF

    IF largest ≠ i
        swap arr[i] with arr[largest]
        heapify(arr, size, largest)
    END IF
END FUNCTION
"""


def heap_sort(arr):
    array_length = len(arr)
    if array_length <= 1:
        return arr
    for i in range(array_length//2 - 1, -1, -1):
        heapify(arr, array_length, i)

    for i in range(array_length-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


array = random.sample(range(10), 10)
arr = [2, 8, 1, 3, 9]
arr1 = [1, 5, 6, 9]
arr2 = [1]
arr3 = []
test_cases = [array, arr, arr1, arr2, arr3]

for case in test_cases:
    print("Before sorting")
    print("==================")
    print(case)
    print("After sorting")
    print(heap_sort(case))
    print("\n")
