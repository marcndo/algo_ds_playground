def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [0, 2, 3, 7, 9, 23]
target = 45
print(linear_search(nums, target))