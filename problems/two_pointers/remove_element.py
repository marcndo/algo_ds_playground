"""
https://leetcode.com/problems/remove-element/description/
Given an integer array with a value, return the number of elements in the array
after dropping all occurrence of the value from the array, the drop should be in-place
nums = [3, 2, 2, 3], val = 3

We would use two pointer technique so that one will scan the array and other will track where to
insert the next element.
For each non_val element, we write it value as indicated by the write_index pointer, then increment it by one
"""


def drop_element(arr, val):
    write_index = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[write_index] = arr[i]
            write_index += 1
    print(arr)
    return write_index


print(drop_element([3, 2, 2, 3], 3))
print(drop_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(drop_element([], 6))

