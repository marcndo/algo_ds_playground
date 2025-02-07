import random

def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        temp = array[i]
        swaped = False
        for j in range(i+1,length):
            if array[j] < array[min_index]:
                min_index = j
        array[i] = array[min_index]
        array[min_index] = temp
        swaped = True
        if not swaped:
            break
    return array
                

array = random.sample(range(10), 10)
print(array)
print(selection_sort(array))