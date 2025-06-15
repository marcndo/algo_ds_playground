import random

def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1):
            temp = array[j]
            if array[j] > array[j+1]:
                array[j] = array[j+1]
                array[j+1] = temp
    return array

# Second approach
def optimize_bubble_sort(array):
    length = len(array)
    for i in range(length):
        swaped = False
        for j in range(length - i - 1):
            if array[j] > array[j+1]:
                temporal = array[j]
                array[j] = array[j+1]
                array[j+1] = temporal
                swaped = True
        if not swaped:
            break
    return array




