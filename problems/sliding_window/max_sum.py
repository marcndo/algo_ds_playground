"""
https://leetcode.com/problems/maximum-subarray/
"""

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = 0
    for i in range(len(nums)):
        if current_sum < 0:  # we check and remove any negative number before a positive number
            current_sum = 0
        current_sum += nums[i]
        max_sum = max(current_sum, max_sum)
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))