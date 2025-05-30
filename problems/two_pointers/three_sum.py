"""
https://leetcode.com/problems/3sum/
Return all possible triplet from a given integer array of numbers that
sum up to zero without repetition

input: nums = [1, -2, 3, -1, 0, 1, -4]
output: [[1, 0, -1],[1, 3, -4], [3, -2, -1]]
input: nums = [1, 8, -9]
output: [[1, 8, -9]]

We would sort the array, then scan through it. We fixed each value from the array, then use
two pointer technique to find two numbers whose sum together with the fixed value equal zero. We then append the values
of the two pointers and the fix value in a list while making sure duplicates are skipped.
"""


def three_sum(nums):
    nums.sort()
    n = len(nums)
    if n == 3:
        sub_total = nums[0] + nums[1] + nums[2]
        if sub_total == 0:
            return [nums]
        else:
            return []
    result = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i+1
        right = n-1
        while left < right:
            sub_total = nums[i] + nums[left] + nums[right]
            if sub_total < 0:
                left += 1
            elif sub_total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result


nums = [-1, -1, 0, 1, 2, 4]
nums1 = [2, -4, 0]
nums2 = [0, 0, 0]
nums3 = list(range(-52, 52))
nums4 = [-1, -8, -4, -9, -4]
nums5 = [3, 9, 7, 5, 9]

test_cases = [nums, nums1, nums2, nums3, nums4, nums5]


for case in test_cases:
    print(three_sum(case))