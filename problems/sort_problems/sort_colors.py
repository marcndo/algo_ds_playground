from random import choices
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that
objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort

input: [2, 0, 0, 1, 2, 2, 0, 1]
output:[0, 0, 0, 1, 1, 2, 2, 2]

input: [1,0, 2]
output: [0, 1, 2]

input: [2, 0]
output: [0, 2]

input: []
output: arr

input: [1]
output: arr
input: [2, 0, 0, 1, 2, 2, 0, 1] 1->[0, 0, 0, 1, 2, 2, 2, 1]2->[0, 0, 0, 1, 2, 2, 2, 1]
3->[0, 0, 0, 1, 2, 2, 2, 1]
first_color_index = 6
i = 6
j = 7
array_length = 8
func sortColor(arr)
    array_length= len(arr)
    if array_length <= 1
        return arr
    for i in range(array_length)
        first_color_index = i
        for j in range(i+1, array_length)
            if arr[j] < arr[array_length]
                first_color_index = j
        if arr[i] != arr[first_index]
            arr[i], arr[array_length] = arr[array_length], arr[i]
"""


def sort_colors(arr_color):
    array_length = len(arr_color)
    if array_length <= 1:
        return arr_color
    for i in range(array_length):
        first_color_index = i
        for j in range(i+1, array_length):
            if arr_color[j] < arr_color[first_color_index]:
                first_color_index = j
        if arr_color[i] != arr_color[first_color_index]:
            arr_color[i], arr_color[first_color_index] = arr_color[first_color_index], arr_color[i]
    return arr_color


arr = choices([0, 1, 2], k=9)
arr1 = [1, 0, 2]
arr2 = [2, 0]
arr3 = []
test_cases = [arr, arr1, arr2, arr3]
for case in test_cases:
    print("Before sorting")
    print(case)
    print("================")
    print("After sorting")
    print(sort_colors(case))
    print("\n")
