
def find_two_sum(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] == target - array[i]:
                return [i, j]


def opt_find_indices(array, target):
    hash_map = {}
    for i in range(len(array)):
        current_key = array[i] 
        if not current_key in hash_map:
            hash_map[target - current_key] = i
        else:
            return [hash_map[current_key], i] 


def optimal_solution(array, target):
    n = len(array)
    i, j = 0, n-1
    while i < j:
        sum_value = array[i] + array[j]
        if sum_value == target:
            return [i, j]
        elif sum_value < target:
            i += 1
        else:
            j += 1
    return 0


array = [2, 7, 11, 15]
target = 26
print(find_two_sum(array, target))

print(opt_find_indices(array, target))
print(optimal_solution(array, target))