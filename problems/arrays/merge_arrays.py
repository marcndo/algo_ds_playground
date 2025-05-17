"""Write a function to merge two sorted arrays and remain sorted
https://leetcode.com/problems/merge-sorted-array/description/
"""


#Brute force approach
#Time complexity (m+n)log(m+n)
def merge_arrays(array1, m, array2, n):
   if not isinstance(array1, list) or isinstance(array2, list):
       print("Input incorrect")
   array1 = array1[:m] + array2
   array1.sort()
   for i in range(m + n):
       array1[i] = array1[i]


def optimal_solution(array1, m, array2, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if array1[i] > array2[j]:
            array1[k] = array1[i]
            i -= 1
        else:
            array1[k] = array2[j]
            j -= 1
        k -= 1

    while j >= 0:
        array1[k] = array2[j]
        k -= 1
        j -= 1


print(merge_arrays([1, 4, 7, 8, 0, 0, 0], 4, [2, 4, 5], 3))
print(optimal_solution([1, 4, 7, 8, 0, 0, 0], 4, [2, 4, 5], 3))