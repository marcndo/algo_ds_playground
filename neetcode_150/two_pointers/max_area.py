
def max_area(nums):
    pass # prefix and suffix maxes approach with O(n) space complexity



#Water quantity would always depend on the min(max_left, max_right)
def maxArea(heights):
    l, r = 0, len(heights) - 1
    result = 0
    max_left, max_right = heights[l], heights[r]
    while l < r:
        if max_left < max_right:
            l += 1
            max_left = max(max_left, heights[l])
            result += max_left - heights[l]
        else:
            r -= 1
            max_right = max(max_right, heights[r])
            result += max_right - heights[r]
    return result 



print(max_area([0,2,0,3,1,0,1,3,2,1]))

print(maxArea([0,2,0,3,1,0,1,3,2,1]))