# Question: https://leetcode.com/problems/container-with-most-water/description/
a = [1,8,6, 4, 2, 0, 8, 1, 10]

#Brute force approach [1,8,6]
def container_with_max_water(array):
    maximum_area = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            area = min(array[i], array[j]) * (j - i)
            if area > maximum_area:
                maximum_area = area
    return f'{maximum_area}m^2'

#Shifting pointers approach a = [1,8,6]
def opt_container_with_max_water(array):
    pointer_1 = 0 
    pointer_2 = len(array)-1 
    maximum_area = 0 
    while pointer_1 < pointer_2:
        area = min(array[pointer_2], array[pointer_1]) * (pointer_2 - pointer_1)
        if area > maximum_area:
            maximum_area = area
        if array[pointer_1] > array[pointer_2]:
            pointer_2 -=1
        else:
            pointer_1 +=1
        
    return f'{maximum_area}m^2'

a = [2, 7]
print(opt_container_with_max_water(a))
print(container_with_max_water(a))
