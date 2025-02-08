# Question: https://leetcode.com/problems/container-with-most-water/description/
a = [1,8,6,2,5,4,8,3,7]

def container_with_max_water(array):
    maximum_area = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            area = min(array[i], array[j]) * (j - i)
            if area > maximum_area: 
                maximum_area = area
    return f'{maximum_area}m^2'
    
print(container_with_max_water(a))
