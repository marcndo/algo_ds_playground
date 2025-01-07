"""Write a scans two arrays and return true if there's a match or false
when there's no match
"""
# Solution one
"""Brute force appraoch: scan through both arrays and compare the
element with the other
This solution works well but it is time inefficient, time complexity
o(len(arr1)*len(arr2)). However, the solution is space efficient
with space complexity of o(1)"""

# def compare_arrays(arr1, arr2):
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 return True
#     return False

arr1 = [2, 5, 8, 3, 9]
arr2 = [1, 2, 7, 11, 12, 18] * 10000000


#Solution two
"""In this second solution, the target would be to optimize the code for
for time efficiency.
Looking at the function below, the time complexity is o(len(arr1) + len(arr2))
while the space complexity is o(len(arr1)).
This code does well in optimizing the time complexity but poorly in space complexity.
"""
# def compare_arrays(arr1, arr2):
#     map_elements = {}
#     for i in arr1:
#         map_elements[i] = True
#     for j in arr2:
#         if j in map_elements.keys():
#             return True
#     return False

#Solution three
"""Another way is to convert one of the array to set.
The time complexity of the code below is O(len(arr1_set) + len(arr2))

"""
# def compare_arrays(arr1, arr2):
#     arr1_set = set(arr1)
#     for j in arr2:
#         if j in arr1_set:
#             return True
#     return False 


def compare_arrays(arr1, arr2):
    return list(set(arr1).intersection(set(arr2)))


print(compare_arrays(arr1, arr2))

