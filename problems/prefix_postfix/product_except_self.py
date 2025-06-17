"""
https://leetcode.com/problems/product-of-array-except-self/submissions/1666662997/
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
=====
prefix_array = []
prefix = 1,
i = 0, prefix = 1, prefix_array = [1]
i = 1, prefix = 1 * nums[1], prefix_array = [1,prefix]
i = 2, prefix = 1 * 2, prefix_array = [1, 1, 2]
i = 3, prefix = 2 * 3, prefix_array = [1, 1, 2, prefix]
prefix_array = [1, 1, 2, 6]
postfix_array = [0, 0, 0, 0]
postfix = 1
i = 3, postfix = 1, postfix_array = [0, 0, 0, 1]
i = 2, postfix = 1 * 4, postfix_array = [0, 0, postfix, 1]
i = 1, postfix = 4 * 3, postfix_array = [0, postfix, 4, 1]
i = 0, postfix = 12 * 2, postfix_array = 24*postfix_array[1], postfix_array = [postfix, 12, 4, 1]
[24, 12, 4, 1]
nums = [1,2,3,4]
prefix = [1,  1,  2, 6]
postfix =[24, 12, 4, 1]
"""


def array_product(nums):
    n = len(nums)
    prefix = 1
    prefix_array = [1] * n  # allocate space ahead of time to avoid potential reallocation in the for loop
    for i in range(1, n):
        prefix *= nums[i-1]
        prefix_array[i] = prefix

    postfix = 1
    for j in range(n-1, -1, -1):
        prefix_array[j] = prefix_array[j] * postfix
        postfix *= nums[j]
    return prefix_array


nums = [1, 2, 3, 4]
print(array_product(nums))


