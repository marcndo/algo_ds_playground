"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Given a sorted array, it is required that we removed all duplicates
in-place and return the new length

We would use two pointer technique since the array is sorted
One pointer would scan the array while the other pointer determine
where we should insert the next unique element.
"""


def remove_duplicate_return_length(arr):
    n = len(arr)
    if n <= 1:
        return n
    write_index = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            arr[write_index] = arr[i]
            write_index += 1
    return write_index

