import random
# Simple bubble sort without optimization
array1 = [5, 2, 6, 1, 9, 0, 1]
array = random.sample(range(10), 10)
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


print(array)
print(optimize_bubble_sort(array))
print(bubble_sort(array))

