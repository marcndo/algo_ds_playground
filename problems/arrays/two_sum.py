
def find_two_sum(array, a):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] == a - array[i]:
                return [i, j]
    


print(find_two_sum([], 89))