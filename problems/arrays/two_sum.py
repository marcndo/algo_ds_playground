
def find_two_sum(array, a):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] == a - array[i]:
                return [i, j]


# We use hash map to solve this problem.
def opt_find_indice(array, target):
    hash_map = {}
    for i in range(len(array)):
        current_key = array[i]
        if not current_key in hash_map:
            hash_map[target - current_key] = i
        else:
            return [hash_map[current_key], i]
    

    

print(find_two_sum([2,7,11,15], 9))

print(opt_find_indice([2,7,11,15], 9))