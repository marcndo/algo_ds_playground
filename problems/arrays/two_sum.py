
def find_two_sum(array, a):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] == a - array[i]:
                return [i, j]


# We use hash map to solve this problem.
def opt_find_indice(array, a):
    hash_map = {}
    for i in range(len(array)):
        if not array[i] in hash_map:
            hash_map[a-array[i]] = i
        else:
            return [hash_map[array[i]], i]
    

    

print(find_two_sum([1, 3, 5, 9, 2], 11))

print(opt_find_indice([1, 3, 5, 9, 2], 11))