def trapRainWater(height):
    if not height:
        return 0
    result = 0
    n = len(height)
    for i in range(n):
        max_left = max_right = height[i]
        for j in range(i):
            max_left = max(max_left, height[j])
        for j in range(i+1, n):
            max_right = max(max_right, height[j])
        result += min(max_left, max_right) - height[i]
    return result


def trap_rain_water(height):
    if not height:
        return 0
    result = 0
    l, r = 0, len(height) - 1
    max_left, max_right = height[l], height[r]
    while l < r:
        if max_left < max_right:
            l += 1
            max_left = max(max_left, height[l])
            result += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            result += max_right - height[r]
    return result

print(trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))



