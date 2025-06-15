import random
"""
You are given an integer array nums and an integer k. Find the maximum subarray
sum of all the subarrays of nums that meet the following conditions:
The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions.
If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.
input: int array, int k
output: k_distinct_max_subarray_sum
array not sorted, max_size 10^6, no duplicates, only positive integers
input: array = [2, 4, 1, 5, 8], k=3
output : 13
input: array = [3, 4, 1], k = 4
output: 0
Initialized max_sum_subarray
Get the sum of the first k elements
Compare with the initial max_sum_subarray and keep the max
Get the next three elements repeat the comparison above.
Repeat for all the possible subarray of size k
Return max_sum_subarray

variance: subarray,
invariance: subarray size, array length

array = [7, 1, 8, 5, 2], k = 3

Brute force approach
====================
We use two pointers, one to scan through the array and the other
to read the  k - 1 elements into a list object
Get the sum of the k - 1 elements plus the fix pointer element into a list
Return max of this list
"""


def get_max_sum_subarray(array, sub_array_length):
    n = len(array)
    if n < sub_array_length:
        return 0
    window_sums = []
    for i in range(n - sub_array_length+1):
        running_sum = 0
        for j in range(i+1, sub_array_length+i):
            if array[j-1] != array[j]:
                running_sum += array[j]
        window_sums.append((running_sum + array[i]))
    return max(window_sums)


# Use sliding window of length k to optimize solution
# inputs: arr = [2, 4, 1, 5, 8], k=3, i = range(0, 3), j = range(i+1, i+3)
# i = 0, j = 1, arr[0] != arr[1], running_sum = arr[1]
# i = 0, j = 2, arr[1] != arr[2], running_sum = arr[1] + arr[2], window_sum =arr[0]] + arr[1] + arr[2]
# i = 1, j = 2, arr[1] != arr[2], running_sum = arr[2]
# i = 1, j = 3, arr[2] != array[3], running_sum = arr[2] + arr[3], window_sum = arr[1] + arr[2] + arr[3]
# i = 2, j = 3, arr[2] != arr[3], running_sum = arr[3]
# i = 2, j = 4, arr[3] != array[4], running_sum = arr[3] + arr[4], window_sum = [arr[2] + arr[3] + arr[4]
# for some i, sum(arr[i:k+i])
# sum_ = sum(arr[i:k]) - arr[i] + arr[i+k]

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return 0
    current_sum = arr[0]
    for i in range(1, k):
        if arr[i] != arr[i-1]:
            current_sum += arr[i]
    max_sum = current_sum
    for i in range(1, n - k + 1):
        if arr[i] != arr[i-1]:
             current_sum -= arr[i-1]
        if arr[i+k-1] != arr[i+k-2]:
            current_sum += arr[i+k-1]
        max_sum = max(current_sum, max_sum)
    return max_sum


k = 3
array = [7, 1, 8, 5, 2]
array1 = [1, 5, 4, 2, 9, 9, 9]
array2 = [1, 5, 4, 2, 9, 9, 9, 10]
array3 = [9, 9, 9]
array4 = random.choices(list(range(50)), k=104)
cases = [array, array1, array2, array3, array4]
for i in range(len(cases)):
    print(f"===Test Case-{i}===")
    print(cases[i])
    print("===Brute Force Result===")
    print(get_max_sum_subarray(cases[i], k))
    print("===Optimal Result===")
    print(max_sum_subarray(cases[i], k))


