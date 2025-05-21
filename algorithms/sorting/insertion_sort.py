import random
# Best in data set that is almost sorted

"""
function insertion_sort(arr)
    length = len(arr)
    if length <= 1
    return arr
    for i in range(1, length)
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
"""


def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i - 1
        current_value = arr[i]
        while j >= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_value
    return arr


array = random.sample(range(10), 10)
print("===Before sorting===")
print(array)
print("====After sorting===")
print(insertion_sort(array))