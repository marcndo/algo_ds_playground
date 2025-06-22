"""
https://leetcode.com/problems/maximum-product-subarray/description/
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


def max_product_subarray(arr):
    current_min, current_max = 1, 1
    result = max(arr)
    for n in arr:
        if n == 0:
            current_max, current_min = 1, 1
            continue
        temp = n * current_max
        current_max = max(n * current_max, n * current_min, n)
        current_min = min(temp, n * current_min, n)
        result = max(result, current_max)
    return result

