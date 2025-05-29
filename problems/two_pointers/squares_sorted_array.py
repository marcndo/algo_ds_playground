import numpy as np
"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/
Given an integer array nums sorted in non-decreasing order,
 return an array of the squares of each number sorted in
 non-decreasing order.

Given a sorted array of integers,return a sorted array of
their squares.

input: nums = [1, 3, 9]
output: [1, 9, 81]
input: nums = [-2, -1, 0, 1, 2]
output: [0, 1, 1, 4, 4]
input: nums = [-10,000, -9999, 8934 9999]
output: [79821156, 99980001, 99980001, 100000000]
input: [-3, -2, -1]
output: [1, 4, 9]
input: [0, 0, 0]
output: [0, 0, 0]
input: nums = [-5, -5, -3, -2, -2, -2]
output: [4, 4, 4, 9, 25, 25]

We would customize the sort method to sort the inputs based on
their absolute values then replace each value by it square
"""

def square_array_sorted(arr):
    n = len(arr)
    if n == 1:
        return [arr[0]**2]
    write_index = n - 1
    result = np.zeros(n, dtype=int)
    left_pointer = 0
    right_pointer = n - 1
    while left_pointer <= right_pointer:
        if abs(arr[left_pointer]) > abs(arr[right_pointer]):
            result[write_index] = arr[left_pointer]**2
            left_pointer += 1
        else:
            result[write_index] = arr[right_pointer]**2
            right_pointer -= 1
        write_index -= 1
    return result


# Test cases
nums = [1, 3, 9]
nums1 = [-2, -1, 0, 1, 2]
nums2 = [-10000, -9999, 8934, 9999]
nums3 = [0, 0, 0]
nums4 = [-5, -5, -3, -2, -2, -2]
nums5 = [7]
nums6 = [79821156, 99980001, 99980001, 100000000]
nums7 = [0, 0, 0]
nums8 = list(range(-5000, 5000))
test_cases = [nums, nums1, nums2, nums3, nums4, nums5, nums6, nums7, nums8]
print("===Before squaring====")
for case in test_cases:
    print(case)
    print("===After squaring===")
    print(square_array_sorted(case))

