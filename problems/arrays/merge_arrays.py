#Write a function to merge two sorted arrays and remain sorted
"""one way is to create an empty list, loop throw the elements, campare 
 them and append them to created list
"""
def merge_arrays(array1, array2):
    return sorted(array1 + array2)


print(merge_arrays([1, 7, 9, 4], [2, 8, 5]))