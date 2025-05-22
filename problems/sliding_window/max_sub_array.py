"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the
subarrays of nums that meet the following conditions:
The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray
meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
============================
input: [1, 6, 2, 7], k = 2
output: [6, 2, 7]
input: [1, 4, 6, 9], k = 3
input: [2, 5, 6]
output: 13, k=3
input: [4, 5, 4]
input: 0
============================
Brute force
FUNCTION max_sum(arr, k)
    n <-- array_length
    IF n < k
        return -1
    END IF
    max_total <-- infinity
    FOR i FROM 0 TO n-k+1
    END FOR
    current_sum <-- 0
        FOR j FROM 0 to k
            current_sum += arr[i+j]
        END FOR
    max_total = max(max_total, current_sum)
    RETURN arr
END FUNCTION
============================================
Optimized
FUNCTION max_k_subarray(arr)
    n <-- array_length
    IF n < k
        RETURN -1
    END IF
    window_sum = sum(arr[:k])
    max_sum = windows_sum
    FOR i FROM 0 to n-k
        windows_sum = windows_sum - arr[i] + arr[i+k]
    END FOR
    max_sum = max(windows_sum, max_sum)
    RETURN max_sum
END FUNCTION

"""


def max_sum(arr, k):
    n = len(arr)
    max_total = float('-inf')
    for i in range(n-k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
        max_total = max(current_sum, max_total)
    return max_total


def max_k_subarray(arr, k):
    n = len(arr)
    if n < k:
        print("Invalid input")
        return -1
    windows_sum = sum(arr[:k])
    max_sum = windows_sum
    for i in range(n-k):
        windows_sum = windows_sum - arr[i] + arr[k+i]
        max_sum = max(max_sum, windows_sum)
    return max_sum


print(max_k_subarray([8, 2, 7, 6], k=2))
print(max_sum([8, 2, 7, 6], k=2))


