def remove_duplicates(nums):
    length = len(nums)
    write = 0
    result = [0] * (length - 1)
    for i in range(length):
        if nums[i] != result[write - 1]:
            result[write] = nums[i]
            write += 1
    return write

def optimal(nums):
    length = len(nums)
    write = 1
    for i in range(1, length):
        if nums[i] != nums[i-1]:
            nums[i], nums[write] = nums[write], nums[i]
            write += 1
    return write
