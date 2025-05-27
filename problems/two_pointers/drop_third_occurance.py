"""
Remove duplicates in-place from a sorted array, but keep at most 2
copies of each unique number.
Array is sorted so, duplicated are adjacent

We use two pointer techniques since array is sorted
One pointer scans the array while the other indicates where the next
unique element should be written
input: nums = [1, 1, 1, 2, 2, 3]
output: 5
"""


def drop_third_occurrance(arr):
    n = len(arr)
    write_index = 2
    for i in range(2, n):
        if arr[i] != arr[write_index - 2]:
            arr[write_index] = arr[i]
            write_index += 1
    print(arr)
    return write_index


print(drop_third_occurrance([1, 1, 1, 2, 2, 3]))