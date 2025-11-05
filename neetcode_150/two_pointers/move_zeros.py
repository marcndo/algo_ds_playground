def move_zeros(nums):
    length = len(nums)
    result = [0] * length
    j = 0
    for i in range(length):
        if nums[i] != 0:
            result[j] = nums[i]
            j += 1
    return result


def optimal(nums):
    write = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write], nums[i] = nums[i], nums[write]
            write += 1
    return nums

print(move_zeros([0,1,0,3,12]))
print(optimal([0,1,0,3,12]))

