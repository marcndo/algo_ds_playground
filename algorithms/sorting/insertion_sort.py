import random
# Best in data set that is almost sorted

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -=1
        array[j+1] = key
    return array


array = random.sample(range(10), 10)
print(array)
print(insertion_sort(array))