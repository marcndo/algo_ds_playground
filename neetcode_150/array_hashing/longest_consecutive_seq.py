#brute force: sort the number, an utilize the fact that consecutive numbers would
# be next to each other

def longest_consecutive_seq(nums):
    new_set = set(nums)
    max_length = 0
    for num in nums:
        if num - 1 not in new_set:
            current_num = num
            current_length = 1
            while current_num + 1 in new_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


