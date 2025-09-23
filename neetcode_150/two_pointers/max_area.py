# We can maximize the area by maximizing the width and the height
# Since the height would always keep getting smaller as the pointer move
# We focus on maximizing the heights
def max_area(nums):
    max_area = 0
    left, right = 0, len(nums) - 1
    while left < right:
        current_area = min(nums[left], nums[right]) * (right - left)
        max_area = max(max_area, current_area)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(max_area([1,8,6,2,5,4,8,3,7]))