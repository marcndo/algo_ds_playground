
def count_sort(nums):
    max_nums = max(nums)
    count = [0] * (max_nums + 1)
    for num in nums:
        count[num] += 1
    sorted_array = []
    for i in range(len(count)):
        if count[i] != 0:
            j = 0
            while j < count[i]:
                sorted_array.append(i)
                j += 1
    return sorted_array