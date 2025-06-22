"""
https://leetcode.com/problems/container-with-most-water/
"""


def maxArea( height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    max_area = 0
    if n == 2:
        return min(height[0], height[1])
    left_pointer, right_pointer = 0, n - 1
    max_area = 0
    while left_pointer < right_pointer:
        area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
        max_area = max(max_area, area)
        if height[left_pointer] > height[right_pointer]:
            right_pointer -= 1
        else:
            left_pointer += 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))



