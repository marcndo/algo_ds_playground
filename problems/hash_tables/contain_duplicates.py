""""
https://leetcode.com/problems/contains-duplicate/
"""

def is_duplicated(arr):
    hash_set = set()
    contain_duplicates = False
    for i in range(len(arr)):
        if arr[i] not in hash_set:
            hash_set.add(arr[i])
        else:
            return True
    return False


print(is_duplicated([1, 2, 3, 4]))


