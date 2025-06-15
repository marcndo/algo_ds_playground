"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.


"""
def trap(height):
    # Edge case: if there are fewer than 3 bars, no water can be trapped
    if len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])

    return water_trapped

# Example input
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = trap(height)
print(f"Water trapped: {result} units")

