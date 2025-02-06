# Simple bubble sort without optimization
array = [5, 2, 6, 1, 9, 0, 1]
def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1):
            temp = array[j]
            if array[j] > array[j+1]:
                array[j] = array[j+1]
                array[j+1] = temp
    return array